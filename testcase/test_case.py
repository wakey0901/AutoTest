from common.operate_excel import *
import unittest
from parameterized import parameterized
from common.send_request import RunMethod
import json
from common.logger import MyLogging
import jsonpath
from common.is_instance import IsInstance
from HTMLTestRunner import HTMLTestRunner
import os
import time

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
file_path = lib_path + "/" + "接口自动化测试.xlsx"  # excel的地址
sheet_name = "测试用例"
log = MyLogging().logger


def getExcelData():
    list = ExcelData(file_path, sheet_name).readExcel()
    return list


# UnitTest类必须继承Case类
class TestCase(unittest.TestCase):

    @parameterized.expand(getExcelData())
    def test_api(self, rowNumber, caseRowNumber, testCaseName, priority, apiName, url, method, parmsType, data,
                 checkPoint, isRun, result):
        if isRun == "Y" or isRun == "y":
            log.info("【开始执行测试用例：{}】".format(testCaseName))
            headers = {"Content-Type": "application/json"}
            data = json.loads(data)  # 字典对象转换为json字符串
            c = checkPoint.split(",")
            log.info("用例设置检查点：%s" % c)
            print("用例设置检查点：%s" % c)
            log.info("请求url：%s" % url)
            log.info("请求参数：%s" % data)
            r = RunMethod()
            res = r.run_method(method, url, data, headers)
            log.info("返回结果：%s" % res)

            flag = None
            for i in range(0, len(c)):
                checkPoint_dict = {}
                checkPoint_dict[c[i].split('=')[0]] = c[i].split('=')[1]
                # jsonpath方式获取检查点对应的返回数据
                list = jsonpath.jsonpath(res, c[i].split('=')[0])
                value = list[0]
                check = checkPoint_dict[c[i].split('=')[0]]
                log.info("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
                print("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
                # 判断检查点数据是否与返回的数据一致
                flag = IsInstance().get_instance(value, check)

            if flag:
                log.info("【测试结果：通过】")
                ExcelData(file_path, sheet_name).write(rowNumber + 1, 12, "Pass")
            else:
                log.info("【测试结果：失败】")
                ExcelData(file_path, sheet_name).write(rowNumber + 1, 12, "Fail")

            # 断言
            self.assertTrue(flag, msg="检查点数据与实际返回数据不一致")
        else:
            unittest.skip("不执行")


if __name__ == '__main__':
    # unittest.main()
    # Alt+Shift+f10 执行生成报告

    # 报告样式1
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = r"D:\PycharmProjects\AutoTest\result\report.html"
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="Esearch接口测试报告", description="测试用例执行情况", verbosity=2)
        runner.run(suite)
