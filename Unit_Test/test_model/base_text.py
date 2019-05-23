#coding=utf-8

from selenium import webdriver
import time
from test_base import base_pack
from test_common import Wait_Time

APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  #定义邮掌柜路径
login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html") #定义登录页面file文件路径

options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class OpenUZG(object):


    t = Wait_Time.Ttime()

    def __init__(self, driver=webdriver.Chrome(chrome_options=options)):
        self.driver = driver
        self.b = base_pack.BasePage(driver)

    def open_uzg(self):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=options)

    def stay_uzg(self):
        """停留在登录页面"""
        self.driver.get(login_url)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def click_button(self):
        """点击登录按钮"""
        self.driver.find_element_by_xpath("//*[@id='loginBtn']").click()

    def button_click(self):
        loc = ("xpath", "//*[@id='loginBtn']")
        self.b.click(loc)

    def text_login(self):
        """点击短信登录"""
        self.driver.find_element_by_xpath("//div[@class='title']/a[2]").click()

    def get_code1(self):
        """短信登录时，点击获取验证码"""
        self.driver.find_element_by_xpath("//*[@id='btnValidateCode']").click()



    def input_username(self, username):
        """输入用户名"""
        self.driver.find_element_by_xpath("//*[@id='username']").clear()
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(str(username))

    def input_usr(self, username):
        loc = ("xpath", "//*[@id='username']")
        self.b.clear_keys(loc)
        for i in username:
            self.t.time1()
            self.b.send_keys1(loc, i)



    def input_password(self, password):
        """输入密码"""
        self.driver.find_element_by_xpath("//*[@id='password']").clear()
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(str(password))

    def input_pwd(self, password):
        loc = ("xpath", "//*[@id='password']")
        self.b.clear_keys(loc)
        for i in password:
            self.t.time1()
            self.b.send_keys1(loc, i)


    def input_mobilenum(self, mobilenum):
        """短信登录输入手机号"""
        self.driver.find_element_by_xpath("//*[@id='mobileNum']").clear()
        self.driver.find_element_by_xpath("//*[@id='mobileNum']").send_keys(str(mobilenum))



    def contrast_result1(self, result):
        """断言机构号输入框文本与预期结果"""
        usernameTip = self.driver.find_element_by_xpath('//*[@id="usernameTip"]/a').text  # 用户名
        print usernameTip
        assert usernameTip == result

    def result1(self, result):
        """断言机构号输入框文本与预期结果"""
        usernameTip = ("xpath", "//*[@id='usernameTip']/a")
        self.b.is_text_in_element1(usernameTip, result)





    def contrast_result2(self, result):
        """断言密码输入框文本与预期结果"""
        passwordTip = self.driver.find_element_by_xpath('//*[@id="passwordTip"]/a').text  # 密码
        print passwordTip
        assert passwordTip == result


    def login1(self, username, password, result):
        """机构号密码登录—机构号输入框错误提示"""
        self.input_usr(username)
        self.input_pwd(password)
        self.button_click()
        time.sleep(2)
        self.result1(result)

    def login2(self, username, password, result):
        """机构号密码登录—密码输入框错误提示"""
        self.input_username(username)
        self.input_password(password)
        self.click_button()
        time.sleep(2)
        self.contrast_result2(result)


if __name__ == "__main__":
    a = OpenUZG()
    time.sleep(2)
    a.input_usr('hah./?')
    time.sleep(2)
    a.input_pwd('123456')
    time.sleep(2)
    a.button_click()
    time.sleep(2)
    a.result1('掌柜登录账号不存在')
    time.sleep(2)
    a.quit_uzg()
