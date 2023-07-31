import scrapy
import mysql.connector
import uuid


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    resources = scrapy.Field()


class ZoomitSpider(scrapy.Spider):
    name = 'zoomit_scrapy'
    start_urls = ['https://www.zoomit.ir/']

    def parse(self, response):

        articles = response.css(
            '.box__BoxBase-sc-1ww1anb-0.eIbCri.pages__LeftModuleBox-ghzl0u-4.gRVxfC')
        for article in articles:
            item = NewsItem()
            
            item['title'] = article.css(
                '.typography__StyledDynamicTypographyComponent-t787b7-0.ibfopD.BrowseArticleListItemDesktop___StyledTypography-sc-1szqe4e-0.hYItiO ::text').getall()

            item['content'] = article.css(
                '.box__BoxBase-sc-1ww1anb-0.eIbCri.pages__LeftModuleBox-ghzl0u-4.gRVxfC p::text').getall()

            item['url'] = article.css(
                '.link__CustomNextLink-sc-1r7l32j-0.iCQspp::attr(href)').getall()
            
        item_list = []
        item_dict = {}
        for title, content, url  in zip(item['title'], item['content'], item['url']):
            item_dict['title'] = title
            item_dict['content'] = content
            item_dict['url'] = url
            item_list.append(item_dict)
            item_dict = {}

            yield response.follow(url, callback=self.parse_news, meta={'title': title, 'content': content, 'item_list': item_list})



    def parse_news(self, response):
        news_item = []
        title = response.meta['title']
        content = response.meta['content']
        tags = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.eMeOeL::text').getall()
        
        resources = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.exnhHg::text').getall()
        
        news_info_dict = {}
        news_info_dict['title'] = title
        news_info_dict['content'] = content
        news_info_dict['tags'] = tags
        news_info_dict['resources'] = resources
        news_item.append(news_info_dict)

        yield {
            'items': news_item
        }

        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ehsan1382',
            database='tek_news_db'
        )

        cursor = connection.cursor()

        for item in news_item:
            title = item['title']
            content = item['content']
            tags = ', '.join(item['tags'])
            resources = ','.join(item['resources'])

            query ="select * from newsmodel where title=%s"
            values = title ,
            cursor.execute(query ,values)

            saved_news = cursor.fetchall()
            
            if saved_news:
                print(f"there is the same news with title : {saved_news} ")
            else:
                query = "INSERT INTO newsmodel (id,title, description, tags , resources ) VALUES (%s,%s, %s,%s , %s)"
                values = (str(uuid.uuid4()),title, content, tags ,resources )

            try:
                cursor.execute(query, values)
                connection.commit()
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                connection.rollback()

        cursor.close()
        connection.close()