from bs4 import BeautifulSoup
from chromedriver import ChromeDriver
import logging
import random
import time


class CountFinder:
    def scraping_count(self):
        try:
            if random.randint(0, 1) == 1:
                time.sleep(2)

            chrome = ChromeDriver()
            chrome.get(url=self.page_url)
            soup1 = BeautifulSoup(chrome.page_source(), "lxml")
            div1 = soup1.find(name="div", attrs={"id": "result_count"})
            count1 = self.extract_count_number(div1.contents)
            self.count = count1
            self.succeed = True
            chrome.quit()

            if random.randint(0, 1) == 1:
                time.sleep(2)
        except Exception as e:
            logging.info('[CountFinder Exception] ' + str(e))
            logging.info('[Error: can not crawl] ' + self.page_url)

    def __init__(self, page_url):
        self.page_url = page_url
        self.count = 0
        self.succeed = False
        self.scraping_count()

    def is_succeed(self):
        return self.succeed

    def get_count(self):
        return self.count

    @staticmethod
    def extract_count_number(div_contents):
        if len(div_contents) == 0:
            return 0
        else:
            div_str = div_contents[0]
            if len(div_str) == 0:
                return 0
            else:
                count_str = div_str.split(' ')[1].replace(',', '')
                return int(count_str)
