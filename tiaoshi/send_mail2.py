import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



username = '342473195@qq.com'
password = 'oagddyqkvclccabe'   # 授权码

# 发送邮箱
sender = '342473195@qq.com'
# 接收邮箱
receiver = 'caohuaqiang@jfcaifu.com'
# 发送邮件主题
subject = 'Python email test'

# 发送的附件
sendfile = open('./report/login.txt', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = "attachment; filename='login.txt'"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()

