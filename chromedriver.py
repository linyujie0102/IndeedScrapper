from selenium import webdriver
from bs4 import BeautifulSoup
import time

class ChromeDriver:
    def __init__(self):
        super().__init__()
        self.PROXY = "127.0.0.1:9150"
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--proxy-server=%s' % self.PROXY)
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--proxy-server=socks5://" + self.PROXY)
        self.chrome = webdriver.Chrome('/Users/linyujie/Desktop/IndeedResumeScraper_python_3_mac_os_x64/chromedriver', chrome_options=chrome_options)

    def get(self, url):
        self.chrome.get(url)

    def page_source(self):
        return self.chrome.page_source

    def quit(self):
        self.chrome.quit()
        time.sleep(1)




# tor = TorDriver()
# page = tor.get(url = "https://www.indeed.com/resumes?q=python&l=CA&cb=jt")
# soup = BeautifulSoup(tor.page_source(), "lxml")
# print(soup.prettify())