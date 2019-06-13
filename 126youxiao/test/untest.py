import unittest
import time

from tools.seleniumder import Selenium
from tools.find_element import Read_config
import HTMLTestRunner
import os
from tools.sned_email import Send_email
from tools.logYeile import Logger

class BaiduTest(unittest.TestCase):
    url = "https://www.baidu.com/"
    s = Selenium(url)

    def setUp(self):
        time.sleep(3)
        self.s.open_browser()

    def tearDown(self):
        time.sleep(3)
        self.s.exit_browser()

    def test_01(self):
        Read_config(self.s.chro).a("sec", "kw", "持币")


sut = unittest.TestSuite()
sut.addTest(BaiduTest("test_01"))
path_mkdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
if not os.path.exists(path_mkdir):
    os.mkdir(path_mkdir)
p = os.path.join(path_mkdir, "sut.html")
fp = open(p, "wb")
r = HTMLTestRunner.HTMLTestRunner(stream=fp, title="这是我的第一次测试报告")
r.run(sut)
s = Send_email("2219334351","2219334351")
o = s.complie_file()
s.send(o)
fp.close()
L=Logger()
L.yiele_log("跟我去拔毛把，我会挑刺",)


