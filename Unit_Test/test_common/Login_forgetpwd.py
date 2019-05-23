# coding=utf-8

from selenium import webdriver
import time
import Wait_Time
from test_base import base_pack

APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe')  # 定义邮掌柜路径
login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\face\\_modules_\\login\\login.html")  # 定义登录页面file文件路径

options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class ForgetPwd(object):

    t = Wait_Time.Ttime()

    """点击忘记密码的各个按钮操作"""
    def open_uzg(self):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=options)
        self.b = base_pack.BasePack(self.driver)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def forget_pwd(self):
        """点击忘记密码"""
        self.t.time2()
        loc = ("xpath", "//div[@id='loginForm']/div[4]/a[2]")
        self.b.click(loc)

    def forget_iframe(self):
        '''切换到忘记密码的iframe上'''
        loc = ("id", "forgetPassWordIframe")
        self.b.switch_iframe(loc)

    def forget_free(self):
        '''释放忘记密码iframe,回到主页面'''
        self.driver.switch_to.default_content()

    def next_step(self):
        """忘记密码中的下一步"""
        loc = ("xpath", "//div[@class='btn']/a")
        self.b.click(loc)
        self.t.time2()

    def get_code2(self):
        """忘记密码中的获取验证码"""
        loc = ("xpath", "//div[@class='txt2 txt']/a")
        self.b.click(loc)
        self.t.time2()

    """定位忘记密码的各个输入框"""
    def input_mobilephone(self, phonenumber):
        """忘记密码—手机号输入"""
        self.t.time2()
        loc = ("xpath", "//*[@id='mobilePhone']")
        self.b.clear_keys(loc)
        for i in phonenumber:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_messgescode(self, messgescode):
        """忘记密码—验证码输入"""
        self.t.time2()
        loc = ("xpath", "//*[@id='messgesCode']")
        self.b.clear_keys(loc)
        for i in messgescode:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_newpwd(self, newpassword):
        """忘记密码—输入新密码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='newpwd']")
        self.b.clear_keys(loc)
        for i in newpassword:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_newpwd2(self, newpassword2):
        """忘记密码—再次输入新密码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='newpwd2']")
        self.b.clear_keys(loc)
        for i in newpassword2:
            self.t.time3()
            self.b.send_keys1(loc, i)

    '''忘记密码验证'''
    def contrast_result7(self, result):
        """断言机构号输入框文本与预期结果"""
        loc = ("xpath", '//*[@class="telmsg msg"]')
        telmsg = self.b.get_text(loc)
        print telmsg
        assert telmsg == result

    def contrast_result8(self, result):
        """断言机构号输入框文本与预期结果"""
        loc = ("xpath", '//*[@class="codemsg msg "]')
        codemsg = self.b.get_text(loc)
        print codemsg
        assert codemsg == result

    def contrast_result9(self, result):
        """断言机构号输入框文本与预期结果"""
        loc = ("xpath", '//*[@class="newpwdmsg msg err"]')
        newpwdmsg = self.b.get_text(loc)
        print newpwdmsg
        assert newpwdmsg == result

    def login7(self, phonenumber, result):
        """忘记密码点击下一步操作，判定手机号输入框下面的提示文本"""
        self.input_mobilephone(phonenumber)
        self.next_step()
        self.contrast_result7(result)

    def login8(self, phonenumber, messgescode, result):
        """忘记密码点击下一步操作，判断验证码输入框下面的提示文本"""
        self.input_mobilephone(phonenumber)
        self.input_messgescode(messgescode)
        self.next_step()
        self.contrast_result8(result)

    def login9(self, phonenumber, messgescode, newpassword, result):
        """忘记密码点击下一步操作，判定输入新密码下面的提示文本"""
        self.input_mobilephone(phonenumber)
        self.input_messgescode(messgescode)
        self.input_newpwd(newpassword)
        self.next_step()
        self.contrast_result9(result)

    def login10(self, phonenumber, result):
        """忘记密码点击获取验证码，判断手机号输入框下面的提示文本"""
        self.input_mobilephone(phonenumber)
        self.get_code2()
        self.contrast_result7(result)

if __name__ == "__main__":
    a = Forget_pwd()
    a.open_uzg()
    a.forget_pwd()
    time.sleep(2)
    a.forget_iframe()
    a.login10("15939000000", "手机号不存在")
    # a.login3("15939000000", "111111", "123qwe", "123qwe", "您输入的手机号码还没有验证通过,不能重新设置新密码,请联系渠道管理员或拨打服务电话!")
    # a.input_mobilephone("15939000000")
    # a.input_messgescode("111111")
    # a.input_newpwd("123qwe")
    # a.input_newpwd2("123qwe")
    # a.next_step()
    # a.contrast_result("您输入的手机号码还没有验证通过,不能重新设置新密码,请联系渠道管理员或拨打服务电话!")
    a.forget_free()
    time.sleep(2)
    # a.quit_uzg()
    # a.login3("15939000000", "11111", "123qwe", "qwe123", "手机号码输入有误")

