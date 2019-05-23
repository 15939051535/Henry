# -*- coding:utf-8 -*-


def f1():
    f = open('test.txt', 'r', encoding='utf-8')
    f.seek(0)
    ls = f.readlines()
    ls[0] = '''const PATH_HOST = 'http://%s:%s' \n''' % ('192.168.113.128', '9090')
    f.close()

    f = open('test.txt', 'w', encoding='utf-8')
    for l in ls:
        f.write(l)
    # f.write('''const PATH_HOST = '%s:%s' ''' % ('192.168.113.128', '9090'))


def main():
    f1()
    pass


if __name__ == '__main__':
    main()
