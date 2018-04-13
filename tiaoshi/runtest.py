import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import os


# ==============定义发送邮件========================
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 编写HTML类型的邮件正文
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    # 连接发送邮件
    user = '342473195@qq.com'
    password = 'oagddyqkvclccabe'

    # 发送邮箱
    sender = '342473195@qq.com'
    # 接收邮箱
    receiver = 'caohuaqiang@jfcaifu.com'


    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out successfully !')





# =============查找测试报告目录，找到最新生成的测试报告文件=================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    print("最新的文件为:  " + lists[-1])
    file_new = os.path.join(testreport, lists[-1])  # os.path.join功能为合并目录
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_dir = './test_case'
    test_report = './reports'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况： ')
    runner.run(discover)

    Newreport = new_report(test_report)
    send_mail(Newreport)    # 发送测试报告
















