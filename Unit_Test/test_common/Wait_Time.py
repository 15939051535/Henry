# coding=utf-8

import random
import time
import random
class Ttime(object):

    def __init__(self, num1=random.uniform(0.3, 1.5), num2=random.randint(2, 3), num3=random.uniform(0.3, 1.1), num4=random.randint(4, 5)):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def time1(self):
        time.sleep(self.num1)

    def time2(self):
        time.sleep(self.num2)

    def time3(self):
        time.sleep(self.num3)

    def time4(self):
        time.sleep(self.num4)


if __name__ == "__main__":
    print random.uniform(0.3, 1.5)
    print random.randint(3, 4)
    print random.uniform(0.3, 1.1)
    print random.randint(1, 2)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print now