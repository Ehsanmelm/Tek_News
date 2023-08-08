import time
import scrapy
import mysql.connector
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MainSpider(scrapy.Spider):
    name = 'zoomit2'
    start_urls = ['https://www.zoomit.ir/archive/?sort=Newest&skip=20']

    def set_chrome_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome(options=self.set_chrome_options())

    def parse(self, response):
        self.driver.get('https://www.zoomit.ir/archive/?sort=Newest&skip=20')

        wait = WebDriverWait(self.driver, 10)
        time.sleep(2)
        count = 0
        while True:
            #  the number 6 is the repetion number for clicking on see more link
            # change this number to get the more news in site
            if count < 6:
                see_more_button = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '.button__Base-kwkpzw-0.fpijDs.BrowseArticleData___StyledButton-sc-1qvnay0-0.eByvXQ')))
                see_more_button.click()
                time.sleep(3)
            else:
                break
            count += 1

        news_links = self.driver.find_elements(
            By.CSS_SELECTOR, '.flex__Flex-le1v16-0.rJAYV a')

        for link in news_links:
            yield scrapy.Request(url=link.get_attribute('href'), callback=self.parse_news, meta={'count': count})

        self.driver.quit()

    def parse_news(self, response):

        title = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.eNoCZh::text').getall()

        tags = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.eMeOeL::text').getall()

        content = response.css(
            '.slug__ArticleContainerMain-sc-1wri6xq-1.WDaAf p::text').getall()

        resources = response.css(
            '.typography__StyledDynamicTypographyComponent-t787b7-0.exnhHg::text').getall()

        connection = mysql.connector.connect(
            host='db',
            user='root',
            password='ehsan1382',
            database='tek_news2'
        )

        cursor = connection.cursor()

    # avoide save repeated news in database
        query = "select * from news_newsmodel where title=%s"
        values = title[0],
        cursor.execute(query, values)

        saved_news = cursor.fetchall()

        if saved_news:
            print(f"there is the same news with title : {saved_news} ")
        else:
            query = "INSERT INTO news_newsmodel (id , title, tags, description, resources ) VALUES (%s ,%s, %s, %s, %s)"
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
