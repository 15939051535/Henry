#coding=utf-8
import unittest
from test_common import HTMLTestRunner
import time

def all_case():  # 待执行用例的目录
    case_dir = "D:\\Unit_Test\\test_case\\login_script"
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="login_test*.py",
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中 for test_suite in discover: for test_case in test_suite:

    for test_suite in discover:
        for test_case in test_suite:  # 添加用例到testunit
            testunit.addTests(test_case)
        print testunit
    return testunit


if __name__ == "__main__":
    # 返回实例
    # runner = unittest.TextTestRunner()

    now = time.strftime('%Y-%m-%M-%H_%M_%S', time.localtime(time.time()))
    report_path = "D:\\Unit_Test\\report\\" + now + "result.html"

    # report_path = "D:\\Unit_Test\\report\\result.html"

    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"自动化测试报告",
                                           description=u"用例执行情况")

    # run所有用例
    runner.run(all_case())
    fp.close()
