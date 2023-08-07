import scrapy
import mysql.connector
import uuid


class NewsItem(scrapy.Item):
    url = scrapy.Field()


class MainSpider(scrapy.Spider):
    name = 'recent_news_scrapy'
    start_urls = ['https://www.zoomit.ir/']

    def parse(self, response):

        articles = response.css(
            '.box__BoxBase-sc-1ww1anb-0.eIbCri.pages__LeftModuleBox-ghzl0u-4.gRVxfC')

        for article in articles:
            item = NewsItem()

            item['url'] = article.css(
                '.link__CustomNextLink-sc-1r7l32j-0.iCQspp::attr(href)').getall()

        for url in item['url']:
            yield response.follow(url, callback=self.parse_news)
            # yield scrapy.Request(url, callback=self.parse_news, meta)

    def parse_news(self, response):

        # title = response.css(
        #     '.typography__StyledDynamicTypographyComponent-t787b7-0.eNoCZh::text').getall()
        title = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.eNoCZh::text').getall()

        tags = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.eMeOeL::text').getall()

        content = response.css(
            '.slug__ArticleContainerMain-sc-1wri6xq-1.WDaAf p::text').getall()

        resources = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.exnhHg::text').getall()
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<< {tags}")
        if len(title) > 0:

            connection = mysql.connector.connect(
                # host='localhost',
                host='db',
                user='root',
                password='ehsan1382',
                # database='tek_test'
                database='tek_news2'
            )

            cursor = connection.cursor()
            # cursor.execute("CREATE DATABASE IF NOT EXISTS tek_news2")

        # avoide save repeated news in database
            query = "select * from news_newsmodel where title=%s"
            values = title[0],
            cursor.execute(query, values)

            saved_news = cursor.fetchall()

            if saved_news:
                print(f"there is the same news with title : {saved_news} ")
            else:
                query = "INSERT INTO news_newsmodel (id , title, tags, description, resources ) VALUES (%s ,%s, %s, %s, %s)"
                # values = ( str(uuid.uuid4()), title[0] , ','.join(tags) , content[0] , ','.join(resources) )
                values = (str(uuid.uuid4()), title[0], ','.join(
                    tags), ','.join(content), ','.join(resources))

            try:
                cursor.execute(query, values)

                connection.commit()

            except Exception as e:
                print(f"Error occurred: {str(e)}")
                connection.rollback()

            cursor.close()
            connection.close()
