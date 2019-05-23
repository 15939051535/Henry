# coding:utf-8
import time
from selenium import webdriver
import unittest



case1 = ["", ""]
case2 = ["", "1"]
case3 = ["1",""]




dcase1 = {"username": "", "password":""}
dcase2 = {"username": "1", "password":""}

class Login_case(unittest.TestCase):
    APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  # 定义邮掌柜路径
    login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html")  # 定义登录页面file文件路径

    options = webdriver.ChromeOptions()
    options.binary_location = APPLICATION_PATH
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_options=cls.options)


    def setUp(self):
        self.driver.get(self.login_url)



    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def login_case(self, username, password):
        '''登录流程'''
        driver = self.driver
        uid = driver.find_element_by_xpath("//*[@id='username']")#定位用户名
        pwd = driver.find_element_by_xpath("//*[@id='password']")#定位密码
        uid.clear()#清用户名输入框内容
        uid.send_keys(username)#传参输入用户名
        time.sleep(3)
        pwd.clear()#清密码输入框内容
        pwd.send_keys(password)#传参输入密码
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='loginBtn']").click()#定位登录按钮的位置并单击
        time.sleep(3)

    def excpet1(self, str1):
        driver = self.driver
        result1 = driver.find_element_by_xpath("//*[@id='usernameTip']/a").text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result1
        if (len(result1) > 1):
            try:
                assert result1 == str1
                print ('Test pass.')
            except Exception as e:
                print ("Test fail.", format(e))




    def excpet2(self, str2):
        driver = self.driver
        result2 = driver.find_element_by_xpath("//*[@id='passwordTip']/a").text
        print result2
        # self.assertEqual(result2, str2)
        try:
            if (len(result2) > 1):
                assert result2 == str2
                print ('Test pass.')
        except Exception as e:
            print ("Test fail.", format(e))


    def excpet3(self, str3):
        driver = self.driver
        result3 = driver.find_element_by_xpath("//*[@id='addres']/div/span").text
        self.assertEqual(result3, str3)

    # def excpet3(self, str3):
    #     driver = self.driver
    #     result3 = driver.find_element_by_xpath("//*[@src='img/logo.jpg']")
    #     self.assertEqual(result3, str3)


    def test_01(self):
        '''输入用户名为空，密码为空，登录失败，提示用户名不能为空'''
        print ("case1")
        self.login_case(*case1)
        self.excpet1(u"用户名能为空")


    def test_02(self):
        '''输入用户名为空，密码为1，登录失败，提示用户名不能为空'''
        self.login_case(*case2)
        self.excpet1(u"用户名不能为空")
        print "case2"

    def test_03(self):
        '''输入用户名为1，密码为空，登录失败，提示密码不能为空'''
        self.login_case(*case3)
        self.excpet2(u"密码不能为空")
        print "case3"


if __name__ == "__main__":
    unittest.main()
