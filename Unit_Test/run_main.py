# coding=utf-8
import unittest
import time
import os
from test_common import HTMLTestRunner1
import logging
from test_base import base_pack
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# 下面三行代码是python2里面为了防止中文乱码、python3可以去掉
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 这个是优化版执行所有用例并收送报告，包括五个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步获取控制台内容打印到日志文件(txt格式)
# 第五步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）


def add_case(case_path, rule):
    """加载所有的测试用例"""
    testunit = unittest.TestSuite()  #定义一个单元测试容器
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
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


# def send_mail(sender, psw, receiver, smtpserver, report_file):
#     """发送最新的测试报告内容"""
#     # 读取测试报告的内容
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     # 定义邮件内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = u"自动化测试报告"
#     msg["from"] = sender
#     msg["to"] = psw
#     # 加上时间戳
#     # msg["date"] = time.strftime('%a, %d %b %Y %H_%M_%S %z')
#     msg.attach(body)
#     # 添加附件
#     att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename= "report.html"'
#     msg.attach(att)
#     # 登录邮箱
#     smtp = smtplib.SMTP()
#     # 连接邮箱服务器
#     smtp.connect(smtpserver)
#     # 用户名密码
#     smtp.login(sender, psw)
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     print 'test report email has send out !'


if __name__ == "__main__":
    # 命令行参数
    name = sys.argv[1]
    # 启动浏览器
    base_pack.browser(name)

    # 上面是写好的四个函数，一般情冴无需修改，叧需改if以下的路径参数就行了
    # 测试用例的路径、匹配规则
    case_path = "D:\\Unit_Test\\test_case"  # 测试用例的路径(可精确到具体的某一个案例上)
    rule = "test*.py"  # 匹配规则(case文件名写法)
    all_case = add_case(case_path, rule)  # 1.加载用例
    # 生成测试报告的路径
    report_path = "D:\\Unit_Test\\report"
    run_case(all_case, report_path)  # 2.执行用例
    # 获取最新的测试报告文件
    report_file = get_report_file(report_path)  # 3.获取最新的测试报告
    # 把控制台输出的内容存放到txt格式的日志文件中
    log_path = os.getcwd() + "\\log\\"+"log.txt"
    get_log_file(log_path)  # 4.把生成的日志文件放在指定路径
    # # 邮箱配置
    # sender = "yoyo@xxx.com"
    # psw = "xxx"
    # # 收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com'
    # receiver = "yoyo@xxx.com"  # 收件人
    # smtp_server = 'smtp.xxx.com'  # 发送邮件服务器
    # send_mail(sender, psw, receiver, smtp_server, report_file)  # 5.最后一步发送报告