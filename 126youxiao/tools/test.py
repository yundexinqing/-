# from selenium import webdriver
# import time
# con = webdriver.Chrome()
# con.get(url = "https://www.baidu.com/")
# con.find_element("id","kw").send_keys("陈文硕")
# time.sleep(2)
# con.quit()

import os


path_mkdir = os.path.join(os.path.dirname(os.path.dirname(__file__)),"log")
if not os.path.exists(path_mkdir):
    os.mkdir(path_mkdir)
print(path_mkdir)
fp = open(os.path.join(path_mkdir,"sut.html"),"wb")
# if not os.path.exists(os.path.join(path,"log")):
#     os.mkdir(os.path.join(path,"log"))