import smtplib
from email.header import Header
from email.mime.text import MIMEText
from config.settings import sut_path
from config.settings import authorization_code

# fromuser = "pjxydxq" + "@163.com"



class Send_email:

    def __init__(self,user,to,email_send="me",email_to="you",email_title="test"):
        self.lis = []
        self.fromuser = user+"@qq.com"
        self.touser = "".join([to,"@qq.com"])
        self.lis.append(self.touser)
        self.email_send = email_send
        self.email_to = email_to
        self.email_titile = email_to

    def open_file(self):
        fp = open(sut_path,"rb")
        f = fp.read()
        return f
    def complie_file(self):
        message = MIMEText(self.open_file(),"html","utf-8")
        message["from"] = Header(self.email_send,'utf-8')
        message["To"] = Header(self.email_to,"utf-8")
        message["Subject"] = Header(self.email_titile,"utf-8")
        return message

    def send(self,message):
        # try:
        smtp = smtplib.SMTP("smtp.qq.com")
        smtp.login(self.fromuser,authorization_code)
        smtp.sendmail(self.fromuser,self.lis,self.complie_file().as_string())
        print("发送成功")
        # except smtplib.SMTPException:
        #     print("error")



