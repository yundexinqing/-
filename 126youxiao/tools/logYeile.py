import logging
from config import settings
import os
import datetime

class Logger:

    timename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ri = os.path.join(settings.log_path,timename) + ".log"

    def yiele_log(self,contex):

        loger = logging.getLogger()
        loger.setLevel(logging.ERROR)
        # 文件
        log = logging.FileHandler(self.ri,encoding="utf-8")
        logs=logging.Formatter('%(asctime)s-%(filename)s|%(message)s')
        log.setFormatter(logs)
        loger.addHandler(log)
        loger.error("'''"+contex+"'''")

