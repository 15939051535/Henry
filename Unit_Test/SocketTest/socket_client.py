#coding=utf-8

import socket
import sys
import time

def close_socket(sock):
    try:
        sock.close()
    except socket.error, e:
        print 'Error close socket:%s' % e
        #else :

#print 'Close socket successfully!'

def flush_socket(sock_fd):
    try:
        sock_fd.flush()
    except socket.error, e:
        print 'Error flush the buffer:%s' % e
        return False
    else:
        # print 'Flush the buffer successfully'
        return True

def communicate(sock):
    while True:
        try:
            # print 'begin to send'
            sock.send('Hello!\r\n')
            # print 'send ok'
        except socket.error, e:
            print 'Error sending data:%s' % e
            close_socket(sock)
            return

        if not flush_socket(sock_fd):
            close_socket(sock)
            return

        while True:
            try:
                # print 'begin to rec'
                buf = sock.recv(2048)
            except socket.error, e:
                print 'Error receiving data:%s' % e
                close_socket(sock)
                return

            if not len(buf):
                print 'Socket has been closed!'
                close_socket(sock)
                return

            if '\r\n' in buf:  # \r\n is the terminator
                break

        print 'The receiving data is', buf

        if not flush_socket(sock_fd):
            close_socket(sock)
            return
        time.sleep(1)


if __name__ == '__main__':

    try:
        socket.setdefaulttimeout(3)
    except socket.error, e:
        print 'Strange error setdefaulttimeout:%s' % e
        sys.exit(1)

    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # sock.setblocking(0)
        except socket.error, e:
            print 'Strange error creating socket:%s' % e
            continue

        print 'Create socket successfully'

        try:
            sock.connect(('localhost', 8650))
        except socket.error, e:
            print 'Connection error:%s' % e
            close_socket(sock)
            continue

        print 'Connect successfully'
        try:
            sock_fd = sock.makefile('rw', 0)
        except socket.error, e:
            print 'Makefile error:%s' % e
            close_socket(sock)
            continue

        communicate(sock)











# import socket
# import time
#
# host = 'localhost'
# port = 8083
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #在客户端开启心跳维护 长连接
# client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
# client.connect((host, port))
#
# while True:
#     client.send('hello Python Internet\r\n'.encode())
#     print 'send data'
#     time.sleep(1)






# import socket               # 导入 socket 模块
#
# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 12345                # 设置端口好
#
# s.connect((host, port))
# print s.recv(1024)
# s.close()