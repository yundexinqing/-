import configparser
from config import settings
from selenium import webdriver
import os
# con = webdriver.Chrome
# con.get()
# con.find_element().send_keys()

class Read_config(object):
    path_con = os.path.join(settings.path, "config", "config.ini")
    con = configparser.ConfigParser()
    read=con.read(path_con)

    def __init__(self,der):
        self.der = der

    def a(self,section,option,hanld):
        str_con = self.con.get(section,option)
        list_con = str_con.split("|")
        by,val=list_con
        # self.der.get("https://www.baidu.com/")
        return self.der.find_element(by,val).send_keys(hanld)



# r = Read_config(webdriver.Chrome())
# r.a("sec","kw","持币")
