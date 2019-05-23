# coding:utf-8
import time
from selenium import webdriver
import pcap

class Login_case():
    APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  # 定义邮掌柜路径
    login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html")  # 定义登录页面file文件路径

    options = webdriver.ChromeOptions()
    options.binary_location = APPLICATION_PATH

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chrome_options=cls.options)
        cls.driver.get(cls.login_url)

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
        time.sleep(2)
        pwd.clear()#清密码输入框内容
        pwd.send_keys(password)#传参输入密码
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='loginBtn']").click()#定位登录按钮的位置并单击
        time.sleep(2)

    def excpet1(self, str1):
        driver = self.driver
        result1 = driver.find_element_by_xpath("//*[@id='usernameTip']/a").text
        # result2 = driver.find_element_by_xpath("//*[@id='passwordTip']/a").text
        # result3 = driver.find_element_by_xpath("//*[@id='addres']/div/span").text
        print result1
        try:
            assert result1 == str1
            print ('Test pass.')
        except Exception as e:
            print ("Test fail.", format(e))




if __name__ == "__main__":
    a = Login_case()

