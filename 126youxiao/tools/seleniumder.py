from selenium import webdriver
from config import settings


url = settings.url
class Selenium(object):
    name = None

    def __init__(self,url):
        self.chro = webdriver.Chrome()
        self.url = url
    def chro_han(self):
        return self.chro

    def open_browser(self):
        self.chro.get(self.url)

    def exit_browser(self):
        self.chro.quit()
