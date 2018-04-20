from bs4 import BeautifulSoup
import requests
from general import *
import logging

class ipFinder:
    def scrape_ip(self):
        try:

            proxies = {'http': "socks5://127.0.0.1:9150"}

            page = requests.get(url=self.url, proxies=proxies)
            
            soup = BeautifulSoup(page.text, "lxml")

            div = soup.find(name="p")
            
            return div.text

        except Exception as e:
            logging.info('ipFinder Exception: ' + str(e))
            return None

    def __init__(self):
        self.url = 'http://www.findmyipaddress.com'

