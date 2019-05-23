# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from test_common import HTMLTestRunner1
import time
import os
import logging

import ast
# from test_common import param_test
# from test_common import param_test


import b

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def add_case(case_path, rule):
    """加载所有的测试用例"""
    # abc = param_test.param()
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(os.getcwd() + "\\test_case\\" + case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中(即测试容器)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)  # 添加用例到testunit
            print testunit
    return testunit


def run_case(all_case, report_path):
    """执行所有的用例, 并把结果写入测试报告"""
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_abspath = os.path.join(report_path, now+"result.html")
    # report_abspath = "D:\\Unit_Test\\report\\"+now+"result.html"
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner1.HTMLTestRunner(stream=fp,
                                            title=u'自动化测试报告,测试结果如下：',
                                            description=u'用例执行情况：')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    """获取最新的测试报告"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def get_log_file(log_path):
    # 清空日志文件
    fo = open(log_path, "w")
    fo.truncate()
    fo.close()
    # 把控制台输出的内容存放到txt格式的日志文件中
    logging.basicConfig(filename=log_path, level=logging.INFO)
    logger = logging.getLogger()
    # fromat = logging.Formatter("%(asctime)s -%(levelname)s - %(message)s")
    fromat = logging.Formatter("%(message)s")
    sh = logging.StreamHandler(stream=sys.stderr)
    sh.setFormatter(fromat)
    logger.addHandler(sh)


def main(argv):
    str = u''
    for val in range(1, len(argv)):
        str += argv[val]
    if str:
        dic = eval(str)
        for key, value in dic.items():
            print key.encode('gbk'), value


if __name__ == "__main__":
    dic = {}
    a = "{'login_script':{'test_login1':[[1,2],[5,6]],'test_login2':[[1,2],[5,6]]}}"
    dic = ast.literal_eval(a)
    b.ab = dic

    # exit(0)

    main(sys.argv)
    # dic = "{u'login_script':{u'test_login1':[[1,2][5,6]],u'test_login2':[[1,2][5,6]]},u'test_login3':[[1,2][5,6]]}, \
    #       u'inbulk_script':{u'test_inbulk2':[[1,2][5,6]], u'test_inbulk5':[[1,2][5,6]]}"

    # a = "{'login_script':{'test_login1':[[1,2],[5,6]],'test_login2':[[1,2],[5,6]]}}"

    # dic = ast.literal_eval(a)

    if u'login_script' in dic:
        case_path = u'login_script'
        # print dic[case_path]
        # print len(dic[u'login_script'])
        for rule in dic[u'login_script']:
            print rule

    case_path = "login_script"  # 测试用例的路径(可精确到具体的某一个案例上)
    rule = "test_login1.py"  # 匹配规则(case文件名写法)
    all_case = add_case(case_path, rule)  # 1.加载用例

    # 生成测试报告的路径
    report_path = "D:\\Unit_Test\\report"
    # report_path = os.getcwd+'\\report"'
    run_case(all_case, report_path)  # 2.执行用例
    # 获取最新的测试报告文件
    report_file = get_report_file(report_path)  # 3.获取最新的测试报告
    # 把控制台输出的内容存放到txt格式的日志文件中
    log_path = os.getcwd() + "\\log\\" + "log.txt"  # "D:\\Unit_Test\\log" + "log.txt"
    get_log_file(log_path)  # 4.把生成的日志文件放在指定路径