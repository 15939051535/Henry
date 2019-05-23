#coding=utf-8

import socket
import sys
import time

#关闭socket服务器连接
def close_socket(sock):
    try:
        sock.close()
    except socket.error, e:
        print 'Error close socket:%s' % e
    else :
        print 'Close socket successfully!'

#刷新文件缓冲器
def flush_socket(sock_fd):
    try:
        #刷新缓冲区的,即将缓冲区中的数据立刻写入文件,同时清空缓冲区,不需要是被动的等待
        sock_fd.flush()
    except socket.error, e:
        print 'Error flush the buffer:%s' % e
        return False
    else:
        # print 'Flush the buffer successfully'
        return True

#接收数据，并发送数据
def communicate(connection):
    while True:

        while True:
            try:
                # print 'begin to rec'
                buf = connection.recv(2048)
            except socket.error, e:
                print 'Error receiving data:%s' % e
                close_socket(connection)
                return

            if not len(buf):
                print 'Socket has been closed!'
                close_socket(connection)
                return

            if '\r\n' in buf:  # \r\n is the terminator
                break

        #打印收到的客户端数据
        print address, buf
        if not flush_socket(sock_fd):
            close_socket(connection)
            return

        try:
            # print 'begin to send'、
            #向客户端发送数据
            connection.send('Welcome!\r\n')
            # print 'send ok'
        except socket.error, e:
            print 'Error sending data:%s' % e
            close_socket(connection)
            return

        if not flush_socket(sock_fd):
            close_socket(connection)
            return


if __name__ == '__main__':
    try:
        #设置socket通信的延时时间
        socket.setdefaulttimeout(6)
    except socket.error, e:
        print 'Strange error setdefaulttimeout:%s' % e
        sys.exit(1)

    try:
        #建立面向连接的socket（TCP连接）
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.setblocking(0)
    except socket.error, e:
        print 'Strange error creating socket:%s' % e
        sys.exit(1)
    print 'Create socket successfully'


    try:
        #绑定主机和端口号
        sock.bind(('localhost', 8650))
    except socket.error, e:
        print 'Strange error bind socket:%s' % e
        sys.exit(1)
    print 'Bind successfully'


    try:
        #监听，最大端口数为5
        sock.listen(5)
    except socket.error, e:
        print 'Strange error begin to listen:%s' % e
        sys.exit(1)
    print 'Server - Begin to listened'

    while True:
        try:
            #建立连接
            connection, address = sock.accept()
        except socket.error, e:
            print 'Strange error begin to accept:%s' % e
            continue

        try:
            #返回对应于套接字的常规文件对象，与内置的open（）函数一样
            #创建一个与该套接字相关连的文件
            sock_fd = connection.makefile('rw', 0)
        except socket.error, e:
            print 'Makefile error:%s' % e
            close_socket(connection)
            continue

        print address, ' - have accepted'

        communicate(connection)





# import socket
#
# BUF_SIZE = 1024
# host = 'localhost'
# port = 8083
#
# #socket套接字，面向连接
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# server.bind((host, port))
# server.listen(1) #接收的连接数
#
# client, address = server.accept()
#
# while True:
#     data = client.recv(BUF_SIZE)
#     print(data.decode())
#     #client.close()




# import socket
#
# s = socket.socket()
#
# host = socket.gethostname()
#
# port = 12345
# s.bind((host, port))
#
# s.listen(5)
#
# while True:
#     c, addr = s.accept()
#     print '连接地址：', addr
#     c.send('欢迎访问菜鸟教程！')
#     c.close()

