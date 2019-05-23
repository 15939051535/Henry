# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from test_common import HTMLTestRunner1
import time
import logging
import os
import sys


def all_case():
    # 加载用例
    # case_dir = os.getcwd() + "\\test_case"  # 待执行用例的路径
    case_dir = "D:\\Unit_Test\\test_case"
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中 for test_suite in discover: for test_case in test_suite:
    for test_suite in discover:
        for test_case in test_suite:  # 添加用例到testunit
            testunit.addTests(test_case)
        print testunit
    return testunit


if __name__ == "__main__":
    a = os.getcwd()
    print a
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 返回实例
    # runner = unittest.TextTestRunner()

    # 生成html格式的测试报告
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_path = (os.getcwd() + "\\report\\" + now + "result.html")
    # report_path = "D:\\Unit_Test\\report\\result.html"d
    fp = open(report_path, "wb")
    runner = HTMLTestRunner1.HTMLTestRunner(stream=fp,
                                            title=u"自动化测试报告",
                                            description=u"用例执行情况")

    # 清空日志文件
    fo = open("D:\\Unit_Test\\log\\log.txt", "w")
    fo.truncate()
    fo.close()
    # 把控制台输出的内容存放到txt格式的日志文件中
    logging.basicConfig(filename=os.getcwd() + "\\log\\" + "log.txt", level=logging.INFO)
    logger = logging.getLogger()
    # fromat = logging.Formatter("%(asctime)s -%(levelname)s - %(message)s")
    fromat = logging.Formatter("%(message)s")
    sh = logging.StreamHandler(stream=sys.stderr)
    sh.setFormatter(fromat)
    logger.addHandler(sh)

    # 执行所有用例(加载的用例)
    runner.run(all_case())
    fp.close()