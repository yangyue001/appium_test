import os
import time
from datetime import datetime
from Util.ParsePageObjectRepository import *
import smtplib
from Util.Log import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from TestScript.run import *


class Emai_cnf:
    def __init__(self,filename):
        global host, user, password, port, sender, title, content
        self.parse_cofig_file = parsepageobjectrepository()
        self.email_items = self.parse_cofig_file.getItemSection('EMAIL')
        host = self.email_items['mail_host']
        user = self.email_items['mail_user']
        password = self.email_items['mail_pass']
        port = self.email_items['mail_port']
        sender = self.email_items['sender']
        title = self.email_items['subject']
        content = self.email_items['content']

        # get receiver list
        self.value = self.email_items['receiver']
        self.receiver = []
        for n in str(self.value).split("/"):
            self.receiver.append(n)

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject =  "接口测试报告" + " " + date

        self.log = MyLog().get_log()
        self.logger = self.log.logger

        self.msg = MIMEMultipart('related')
        self.filename = filename

    def header_cfg(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def content_cfg(self):
        '''
                with open(os.path.join(project_path,'TestData','emailStyle.txt')) as f:
            content = f.read()

        content_plain = MIMEText(content,'html', 'UTF-8')
        self.msg.attach(content_plain)


        :return:
        '''


        content_plain = MIMEText(content)
        self.msg.attach(content_plain)


    def attachment_cfg(self):
        att1 = MIMEText(open(self.filename, 'rb').read(), 'base64', 'utf-8')

        self.msg.attach(att1)

    def img_cfg(self):
        print('')

    def send_email(self):
        self.header_cfg()
        self.content_cfg()
        self.attachment_cfg()
        try:
            smtp = smtplib.SMTP_SSL(host,port)
            smtp.login(user,password)
            smtp.sendmail(sender,self.receiver,self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")


        except Exception as e :
            self.logger.error(str(e))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self,file):
        pass
    @staticmethod
    def get_email(file):
        if MyEmail.email is None:

            MyEmail.mutex.acquire()
            MyEmail.email = Emai_cnf(file)
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == '__main__':
    email = MyEmail.get_email()
    email.send_email()