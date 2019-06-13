import os
url = "https://www.baidu.com/"

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 授权码
authorization_code = "hhntwktgfnjdeaia"

#报告路径
sut_path = r"E:\shixun\126youxiao\log\sut.html"

log_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(log_path,"log","logs")
