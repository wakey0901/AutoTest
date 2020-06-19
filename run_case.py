import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.send_email import send_email

# 获取当前py文件绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))


# 1: 加载测试用例
def all_test():
    case_path = os.path.join(cur_path, "testcase")
    suite = unittest.TestLoader().discover(start_dir=case_path, pattern="test_*.py", top_level_dir=None)
    return suite


# 2: 执行测试用例
def run():
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # 测试报告路径
    file_name = os.path.join(cur_path, "report") + "/" + now + "-report.html"
    f = open(file_name, "wb")
    runner = HTMLTestRunner(stream=f, title="接口自动化测试报告",
                            description="环境：windows 10 浏览器：chrome",
                            tester="wangzhijun")
    runner.run(all_test())
    f.close()


# 3: 获取最新的测试报告
def get_report(report_path):
    list = os.listdir(report_path)
    list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
    print("测试报告：", list[-1])
    report_file = os.path.join(report_path, list[-1])
    return report_file


# 4: 发送邮件
def send_mail(subject, report_file, file_names):
    # 读取测试报告内容，作为邮件的正文内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    send_email(subject, mail_body, file_names)


if __name__ == "__main__":
    run()
    report_path = os.path.join(cur_path, "report")  # 测试报告路径
    report_file = get_report(report_path)  # 测试报告文件
    subject = "Esearch接口测试报告"  # 邮件主题
    file_names = [report_file]  # 邮件附件
    # 发送邮件
    send_mail(subject, report_file, file_names)
