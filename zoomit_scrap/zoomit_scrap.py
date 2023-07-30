import scrapy
import mysql.connector

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()


class ZoomitSpider(scrapy.Spider):
    name = 'zoomit_scrapy'
    start_urls = ['https://www.zoomit.ir/']

    def parse(self, response):

        articles = response.css(
            '.box__BoxBase-sc-1ww1anb-0.eIbCri.pages__LeftModuleBox-ghzl0u-4.gRVxfC')
        for article in articles:
            item = NewsItem()
            exit
            item['title'] = article.css(
                '.typography__StyledDynamicTypographyComponent-t787b7-0.ibfopD.BrowseArticleListItemDesktop___StyledTypography-sc-1szqe4e-0.hYItiO ::text').getall()

            item['content'] = article.css(
                '.box__BoxBase-sc-1ww1anb-0.eIbCri.pages__LeftModuleBox-ghzl0u-4.gRVxfC p::text').getall()

            item['url'] = article.css(
                '.link__CustomNextLink-sc-1r7l32j-0.iCQspp::attr(href)').getall()
