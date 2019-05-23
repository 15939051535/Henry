# coding=utf-8

from selenium import webdriver
import time
from test_base import base_pack
from test_common import Wait_Time

APPLICATION_PATH = 'C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe'  # 定义邮掌柜路径
# 定义登录页面file文件路径
login_url = "file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\face\\_modules_\\login\\login.html"

options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class OpenUZG(object):

    t = Wait_Time.Ttime()

    def open_uzg(self):
        '''打开邮掌柜'''
        self.driver = webdriver.Chrome(chrome_options=options)
        self.b = base_pack.BasePack(self.driver)

    def stay_uzg(self):
        """刷新邮掌柜登录页面"""
        self.driver.get(login_url)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def click_button(self):
        """点击登录按钮"""
        self.t.time2()
        loc = ("xpath", "//*[@id='loginBtn']")
        self.b.click(loc)

    def text_login(self):
        """点击短信登录"""
        self.t.time2()
        loc = ("xpath", "//div[@class='title']/a[2]")
        self.b.click(loc)

    def get_code1(self):
        """短信登录时，点击获取验证码"""
        loc = ("xpath", "//*[@id='btnValidateCode']")
        self.b.click(loc)
        self.t.time2()

    def input_username(self, username):
        """输入用户名"""
        self.t.time2()
        loc = ("xpath", "//*[@id='username']")
        self.b.clear_keys(loc)
        for i in username:
            self.t.time1()
            self.b.send_keys1(loc, i)

    def input_password(self, password):
        """输入密码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='password']")
        self.b.clear_keys(loc)
        for i in password:
            self.t.time1()
            self.b.send_keys1(loc, i)

    def input_mobilenum(self, mobilenum):
        """短信登录输入手机号"""
        self.t.time2()
        loc = ("xpath", "//*[@id='mobileNum']")
        self.b.clear_keys(loc)
        for i in mobilenum:
            self.t.time1()
            self.b.send_keys1(loc, i)

    def input_validatecode(self, validatecode):
        """短信登录输入验证码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='validateCode']")
        self.b.clear_keys(loc)
        for i in validatecode:
            self.t.time1()
            self.b.send_keys1(loc, i)

    def contrast_result1(self, result):
        """断言机构号输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='usernameTip']/a")
        usernameTip = self.b.get_text(loc)
        print usernameTip
        assert usernameTip == result

    def contrast_result2(self, result):
        """断言密码输入框文本与预期结果"""
        loc = ("xpath", '//*[@id="passwordTip"]/a')
        passwordTip = self.b.get_text(loc)
        print passwordTip
        assert passwordTip == result

    def contrast_result3(self, result):
        """断言登录成功后邮掌柜首页文本与预期结果"""
        loc = ("xpath", '//*[@id = "addres"]/div/span')
        loginsuccessTip = self.b.get_text(loc)
        print loginsuccessTip
        assert loginsuccessTip == result

    def contrast_result4(self, result):
        """断言短信登录手机号输入框文本与预期结果"""
        loc = ("xpath", '//*[@id="mobileNumTip"]/a')
        mobileNumTip = self.b.get_text(loc)
        print mobileNumTip
        assert mobileNumTip == result

    def contrast_result5(self, result):
        """断言短信登录验证码输入框文本与预期结果"""
        loc = ("xpath", '//*[@id="validateCodeTip"]/a')
        validateCodeTip = self.b.get_text(loc)
        print validateCodeTip
        assert validateCodeTip == result


    def login1(self, username, password, result):
        """机构号密码登录—机构号输入框错误提示"""
        self.input_username(username)
        self.input_password(password)
        self.click_button()
        time.sleep(2)
        self.contrast_result1(result)

    def login2(self, username, password, result):
        """机构号密码登录—密码输入框错误提示"""
        self.input_username(username)
        self.input_password(password)
        self.click_button()
        time.sleep(2)
        self.contrast_result2(result)

    def login3(self, username, password, result):
        """密码登录—登录成功判定"""
        self.input_username(username)
        self.input_password(password)
        self.click_button()
        time.sleep(2)
        self.contrast_result3(result)

    def login4(self, mobilenum, validatecode, result):
        """短信登录—点击登录按钮后，手机号码输入框判定"""
        self.input_mobilenum(mobilenum)
        self.input_validatecode(validatecode)
        self.click_button()
        time.sleep(2)
        self.contrast_result4(result)

    def login5(self, mobilenum, validatecode, result):
        """"短信登录—点击登录按钮后，验证码输入框判定"""
        self.input_mobilenum(mobilenum)
        self.input_validatecode(validatecode)
        self.click_button()
        time.sleep(2)
        self.contrast_result5(result)

    def login6(self, mobilenum, result):
        """短信登录—点击获取验证码后，手机号码输入框判定"""
        self.input_mobilenum(mobilenum)
        self.get_code1()
        time.sleep(2)
        self.contrast_result4(result)


if __name__ == "__main__":
    a = OpenUZG()
    a.open_uzg()
    time.sleep(2)
    a.login1("haha" ,"123456", u"掌柜登录账号不存在")
    time.sleep(2)
    a.quit_uzg()