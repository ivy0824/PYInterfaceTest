#!/usr/bin/python3
import datetime
import os
import readConfig
import getpathInfo
import smtplib
from email.mime.text import MIMEText
from email.header import Header

read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
sender = read_conf.get_email('sender')  # 从配置文件中读取，邮件抄送人
pwd = read_conf.get_email('pwd')
receiver = read_conf.get_email('receiver')  # 从配置文件中读取，邮件收件人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径


class send_email():
    def send(self):
        # QQ邮箱的第三方服务
        mail_host = "smtp.mxhichina.com"
        mail_port = 465

        # 邮件内容
        mail_msg = '------test------'

        # 邮件正文
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式（html为设置html格式），第三个 utf-8 设置编码
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
        message['To'] = Header("测试", 'utf-8')  # 接收者

        email_subject = str(datetime.datetime.now())[0:19] + '%s' % subject  # 邮件主题
        message['Subject'] = Header(email_subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
            smtpObj.login(sender, pwd)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':  # 运营此文件来验证写的send_email是否正确
    print(subject)
    send_email().send()
    print("send email ok!!!!!!!!!!")

