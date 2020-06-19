from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from config import read_email_config
import smtplib


def send_email(subject, mail_body, file_names=list()):
    # 获取邮件相关信息
    smtp_server = read_email_config.smtp_server
    port = read_email_config.port
    user_name = read_email_config.user_name
    password = read_email_config.password
    sender = read_email_config.sender
    receiver = read_email_config.receiver

    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = user_name
    msg["To"] = receiver
    msg.attach(body)

    # 附件:附件名称用英文
    for file_name in file_names:
        att = MIMEText(open(file_name, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = "attachment;filename='report.html'"  # filename为邮件中附件显示的名字
        msg.attach(att)

    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(user_name, password)
        smtp.sendmail(sender, receiver.split(','), msg.as_string())
    except Exception as e:
        print(e)
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


if __name__ == '__main__':
    subject = "测试标题"
    mail_body = "测试本文"
    receiver = "780156051@qq.com,hb_zhijun@163.com"  # 接收人邮件地址 用逗号分隔
    file_names = [r'D:\PycharmProjects\AutoTest\result\2020-02-23 13_38_41report.html']
    send_email(subject, mail_body, receiver, file_names)
