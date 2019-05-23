# -*- coding:utf-8 -*-
import urllib
import re

# 百度图片URL解码
# http://blog.csdn.net/hbuxiaoshe/article/details/44780653
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

char_table = {ord(key): ord(value) for key, value in char_table.items()}
re_url = re.compile(r'"objURL":"(.*?)"')


# 解码
def decode(url):
    for key, value in str_table.items():
        url = url.replace(key, value)
    return url.translate(char_table)


def main():
    url = r'ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bw6p2tup_z&e3BvgAzdH3FUfj6FtsjfAzdH3Ft4w2jfAzdH3Fr6517vpAzdH3Fwsk7456t2tgwsAzdH3F8b8jn9cw1jbu99k0b8098091dvudlccl_z&e3B3r2'
    print(decode(url))
    pass


if __name__ == '__main__':
    main()