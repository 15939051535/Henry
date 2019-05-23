# -*- coding: utf-8 -*-
import json
import os
import sys


def main(argv):
    str = u''
    for val in range(1, len(argv)):
        str += argv[val]
    # print "脚本名：", argv[0]
    # for i in range(1, len(argv)):
    #     # print u"参数".decode('utf-8').encode('unicode_escape'), i, argv[i]
    #     print u"参数".encode('gbk'), i, argv[i]
    # for arg in argv:
    #     print arg
    if str:
        dic = eval(str)
        for key, value in dic.items():
            print key.encode('gbk'), value


if __name__ == '__main__':
    main(sys.argv)
    dic = {u'1': [u'1.1', u'1.2'], u'2': [u'2.1'], u'3': [u'3.1']}
    dic1 = {u'login_script': [u'test_login2', u'test_login3'], u'inbulk_script': [u'test_inbulk2', u'test_inbulk5']}
    if u'login_script' in dic1:
        case_path = u'login_script'
        print dic1[case_path]
        print len(dic1[u'login_script'])
        rule = dic1[case_path][0]
        print rule

        # for rule in dic1[case_path]:
        #     print rule

    # if u'inbulk_script' in dic1:
    #     print dic1[u'inbulk_script']
    # if u'storage_script' in dic1:
    #     print dic1[u'storage_script']

    # m = dic1.get(u'login_script', 1)
    # print m
    # print m[0]
    # print m[1]
    # n = dic.get(u'storage_script', 1)
    # print n
