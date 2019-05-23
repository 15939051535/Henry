# -*- coding:utf-8 -*-
import logging
import time
import socket


def get_host_ip() -> str:
    # 获取本机ip地址
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


class Log(object):
    file_name = './log/myapp_%s.log' % time.strftime('%Y-%m-%d', time.localtime(time.time()))

    handler = logging.FileHandler(filename=file_name, encoding='UTF-8')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S ',
                        handlers=(handler,))

    @classmethod
    def info(cls, msg):
        logging.info(msg)


config = {

    'page_size': 20,
    'port': '9090',
    'host': get_host_ip(),
    'env': 'beta',
}


