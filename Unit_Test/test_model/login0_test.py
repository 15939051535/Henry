#coding=utf-8

from selenium import webdriver
import time
from test_common import Wait_Time

class OpenUZG(object):
    APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  #定义邮掌柜路径
    login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html") #定义登录页面file文件路径

    options = webdriver.ChromeOptions()
    options.binary_location = APPLICATION_PATH

    b = Wait_Time.Ttime()

    """打开关闭邮掌柜及各按钮操作"""
    def open_uzg(self):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def stay_uzg(self):
        """停留在登录页面"""
        self.driver.get(self.login_url)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def click_button(self):
        self.b.time2()
        """点击登录按钮"""
        self.driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        self.b.time2()

    def text_login(self):
        """点击短信登录"""
        self.driver.find_element_by_xpath("//div[@class='title']/a[2]").click()

    def get_code1(self):
        """短信登录时，点击获取验证码"""
        self.driver.find_element_by_xpath("//*[@id='btnValidateCode']").click()

    def forget_pwd(self):
        """点击忘记密码"""
        self.driver.find_element_by_xpath("//*[@class='forgetpwd']").click()

    def next_step(self):
        """忘记密码中的下一步"""
        self.driver.find_element_by_xpath("//*[@class='btn'/a]").click()

    def get_code2(self):
        """忘记密码中的获取验证码"""
        self.driver.find_element_by_xpath("//*[@id='messgesCode'/a]").click()


    """各输入框定位及输入"""
    def input_username(self, username):
        self.b.time2()
        """输入用户名"""
        self.driver.find_element_by_xpath("//*[@id='username']").clear()
        # self.driver.find_element_by_xpath("//*[@id='username']").send_keys(str(username))
        for i in username:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='username']").send_keys(i)

    def input_password(self, password):
        self.b.time2()
        """输入密码"""
        self.driver.find_element_by_xpath("//*[@id='password']").clear()
        # self.driver.find_element_by_xpath("//*[@id='password']").send_keys(str(password))
        for i in password:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='password']").send_keys(i)

    def input_mobilenum(self, mobilenum):
        self.b.time2()
        """短信登录输入手机号"""
        self.driver.find_element_by_xpath("//*[@id='mobileNum']").clear()
        # self.driver.find_element_by_xpath("//*[@id='password']").send_keys(str(password))
        for i in mobilenum:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='mobileNum']").send_keys(i)

    def input_validatecode(self, validatecode):
        self.b.time2()
        """短信登录输入验证码"""
        self.driver.find_element_by_xpath("//*[@id='validateCode']").clear()
        # self.driver.find_element_by_xpath("//*[@id='password']").send_keys(str(password))
        for i in validatecode:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='validateCode']").send_keys(i)

    def input_mobilephone(self, mobilephone):
        self.b.time2()
        """忘记密码—手机号输入"""
        self.driver.find_element_by_xpath("//*[@id='mobilePhone']").clear()
        self.driver.find_element_by_xpath("//*[@id='mobilePhone']").send_keys(str(mobilephone))

    def input_messgescode(self, messgescode):
        self.b.time2()
        """忘记密码—验证码输入"""
        self.driver.find_element_by_xpath("//*[@id='messagesCode']").clear()
        self.driver.find_element_by_xpath("//*[@id='messagesCode']").send_keys(str(messgescode))

    def input_newpwd(self, newpassword):
        self.b.time2()
        """忘记密码—输入新密码"""
        self.driver.find_element_by_xpath("//*[@id='newpwd']").clear()
        self.driver.find_element_by_xpath("//*[@id='newpwd']").send_keys(str(newpassword))

    def input_newpwd2(self, newpassword2):
        self.b.time2()
        """忘记密码—再次输入新密码"""
        self.driver.find_element_by_xpath("//*[@id='newpwd2']").clear()
        self.driver.find_element_by_xpath("//*[@id='newpwd2']").send_keys(str(newpassword2))


    """元素文本的提取做断言"""
    def contrast_result(self, result):
        """断言元素文本与预期结果"""
        usernameTip = self.driver.find_elements_by_xpath('//*[@id="usernameTip"]/a')  #用户名
        passwordTip = self.driver.find_elements_by_xpath('//*[@id="passwordTip"]/a')  #密码
        loginsuccessTip = self.driver.find_elements_by_xpath('//*[@id = "addres"]/div/span')  #邮掌柜首页
        mobileNumTip = self.driver.find_elements_by_xpath('//*[@id="mobileNumTip"]/a')  #短信登录手机号
        validateCodeTip = self.driver.find_elements_by_xpath('//*[@id="validateCodeTip"]/a')  # 短信登录验证码
        telmsg = self.driver.find_elements_by_xpath('//*[@class="telmsg msg"]')  # 忘记密码手机号
        codemsg = self.driver.find_elements_by_xpath('//*[@class="codemsg msg"]')  # 忘记密码验证码
        newpwdmsg = self.driver.find_elements_by_xpath('//*[@class="newpwdmsg msg err"]')  # 忘记密码输入新密码
        newpwd2msg = self.driver.find_elements_by_xpath('//*[@class="newpwd2msg msg err"]')  # 忘记密码再次输入新密码
        iimsg = self.driver.find_elements_by_xpath('//*[@class="ii-msg"]')  # 忘记密码点击下一步提示

        try:
            if ( len(usernameTip) > 1 ):
                self.assertEqual(usernameTip[0].text, result)

            if ( len(passwordTip) > 1 ):
                self.assertEqual(passwordTip[0].text, result)

            if ( len(loginsuccessTip) > 1 ):
                self.assertEqual(loginsuccessTip[0].text, result)

            if ( len(mobileNumTip) > 1 ):
                self.assertEqual(mobileNumTip[0].text, result)

            if ( len(validateCodeTip) > 1 ):
                self.assertEqual(validateCodeTip[0].text, result)

            if ( len(telmsg) > 1 ):
                self.assertEqual(telmsg[0].text, result)

            if ( len(codemsg) > 1 ):
                self.assertEqual(codemsg[0].text, result)

            if ( len(newpwdmsg) > 1 ):
                self.assertEqual(newpwdmsg[0].text, result)

            if ( len(newpwd2msg) > 1 ):
                self.assertEqual(newpwd2msg[0].text, result)

            if ( len(iimsg) > 1 ):
                self.assertEqual(iimsg[0].text, result)

        except AssertionError:
            print (u"断言出现异常错误")

    """各登录方法的整合"""
    def login(self, username, password, result):
        """正常登录公共方法"""
        # print username, password, result
        self.input_username(username)
        self.input_password(password)
        self.click_button()
        self.contrast_result(result)

    def login1(self, mobilenum, validatecode, result):
        """短信登录的方法"""
        self.input_mobilenum(mobilenum)
        self.input_validatecode(validatecode)
        self.click_button()
        self.contrast_result(result)

    def login2(self, mobilenum, validatecode, result):
        """短信登录点击获取验证码"""
        self.input_mobilenum(mobilenum)
        self.input_validatecode(validatecode)
        self.get_code1()
        self.contrast_result(result)

    def login3(self, mobilephone, messgescode, newpassword, newpassword2,result):
        """忘记密码点击下一步操作"""
        self.input_mobilephone(mobilephone)
        self.input_messgescode(messgescode)
        self.input_newpwd(newpassword)
        self.input_newpwd(newpassword2)
        self.next_step()
        self.contrast_result(result)

    def login4(self, mobilephone, messgescode, newpassword, newpassword2,result):
        """忘记密码点击获取验证码"""
        self.input_mobilephone(mobilephone)
        self.input_messgescode(messgescode)
        self.input_newpwd(newpassword)
        self.input_newpwd(newpassword2)
        self.get_code2()
        self.contrast_result(result)


if __name__ == "__main__":
    a = OpenUZG()
    a.open_uzg()
    time.sleep(2.5)
    a.forget_pwd()
    a.input_mobilephone("15939051535")
    a.input_messgescode("111111")
    a.input_newpwd("123qwe")
    a.input_newpwd2("qwe123")
    a.next_step()
    a.contrast_result("两次密码输入不一致")
    # a.login3("15939051535", "111111", "123qwe", "qwe123" , "两次密码输入不一致")
    time.sleep(2.5)
    a.quit_uzg()