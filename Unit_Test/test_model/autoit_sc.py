#coding=utf-8

import time
import autoit
from selenium import webdriver
import unittest
import ddt
from test_common import ReadExcel



class UZG(object):
    APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  #定义邮掌柜路径
    login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html") #定义登录页面file文件路径

    options = webdriver.ChromeOptions()
    options.binary_location = APPLICATION_PATH


    def open_uzg(self):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def click_button(self):
        """点击登录按钮"""
        self.driver.find_element_by_xpath("//*[@id='loginBtn']").click()

    def input_username(self):
        time.sleep(2)
        """输入用户名"""
        self.driver.find_element_by_xpath("//*[@id='username']").clear()
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys('wanghengli')


    def input_password(self):
        time.sleep(2)
        """输入密码"""
        self.driver.find_element_by_xpath("//*[@id='password']").clear()
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys('hengli')


    def module_autoit(self):
        # autoit.mouse_click("left",755,32,1)
        # time.sleep(2)
        # autoit.mouse_move(781, 61, -1)
        # time.sleep(2)
        # autoit.mouse_click("left",781,61,1)
        # time.sleep(2)
        #点击进入收银台
        time.sleep(2)
        autoit.mouse_click("left", 203, 36, 1)
        time.sleep(2)
        autoit.send("1")
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(2)
        autoit.mouse_click("left", 595, 262, 1)
        time.sleep(2)
        autoit.send("8")
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(2)
        autoit.mouse_click("left", 908, 808, 1)
        time.sleep(2)
        autoit.send("{F8}")
        time.sleep(2)
        autoit.send("{ENTER}")






    # def huiyuan(self,key1):
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//*[@id='vIp']").clear()
    #     self.driver.find_element_by_xpath("//*[@id='vIp']").send_keys(key1)
    # def shangpinma(self,key2):
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//*[@id='barCode']").clear().send_keys(key2)
    #     time.sleep(2)
    #     autoit.send("{ENTER}")
    # def danjia(self):
    #     self.driver.find_element_by_xpath("//*[@class='l3 pirce']").click()
    #     time.sleep(2)
    #     autoit.send("8")







    def module(self):
        self.open_uzg()
        self.input_username()
        self.input_password()
        self.click_button()
        time.sleep(2)
        self.module_autoit()


if __name__ == "__main__":
    a = UZG()
    a.open_uzg()
    a.input_username()
    a.input_password()
    a.click_button()
    time.sleep(2)
    a.module_autoit()



