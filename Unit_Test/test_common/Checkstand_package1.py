#coding=utf-8

from selenium import webdriver
import time
import Wait_Time
import autoit


APPLICATION_PATH = 'C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe'  # 定义邮掌柜路径
options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class shyt(object):
    b = Wait_Time.Ttime()

    def open_uzg(self, username='9999999905', password='999905'):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=options)
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@id='username']").clear()
        # self.driver.find_element_by_xpath("//*[@id='username']").send_keys(str(username))
        for i in username:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='username']").send_keys(i)
        self.b.time2()
        """输入密码"""
        self.driver.find_element_by_xpath("//*[@id='password']").clear()
        # self.driver.find_element_by_xpath("//*[@id='password']").send_keys(str(password))
        for i in password:
            self.b.time1()
            self.driver.find_element_by_xpath("//*[@id='password']").send_keys(i)
        self.b.time2()
        """点击登录按钮"""
        self.driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        time.sleep(2)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

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

    def click_button(self):
        self.b.time2()
        """点击登录按钮"""
        self.driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        time.sleep(2)

    def click_btn(self):
        self.b.time2()
        """点击快捷键"""
        self.driver.find_element_by_xpath("//*[@id='btnF2']").click()
        time.sleep(2)

    def click_shyt(self):
        """点击收银台"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@id='hd_nav']/li[1]").click()

    def click_billLink(self):
        """点击挂单"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@id='billLink']").click()

    def click_closequdana(self):
        """关闭挂单窗口"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-title']").click()

    def click_qudana(self):
        """取单1"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[1]").click()

    def click_billdela(self):
        """删除单1"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[1]/i[3]").click()

    def click_qudanb(self):
        """取单2"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[2]").click()

    def click_billdelb(self):
        """删除单2"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[2]/i[3]").click()

    def click_qudanc(self):
        """取单3"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[3]").click()

    def click_billdelc(self):
        """删除单3"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='bill-content']/span[3]/i[3]").click()

    def click_sure(self):
        """点击散货商品确定按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='yzg-btn fr sure']").click()
        time.sleep(2)

    def click_cancle(self):
        """点击返回收银台"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='yzg-btn yzg-btn-white cancel-btn']").click()
        time.sleep(2)

    def input_shytiframe(self):
        '''切换到收银台的iframe上'''
        self.driver.switch_to.frame("shyt")

    def input_vip(self, vip):
        self.b.time2()
        """输入会员号码"""
        self.driver.find_element_by_xpath("//*[@id='vIp']").clear()
        self.driver.find_element_by_xpath("//*[@id='vIp']").send_keys(vip)

    def input_barCode(self, barCode):
        self.b.time2()
        """输入商品编码"""
        self.driver.find_element_by_xpath("//*[@id='barCode']").clear()
        self.driver.find_element_by_xpath("//*[@id='barCode']").send_keys(barCode)

    def click_jiesuan(self):
        self.b.time2()
        """点击结算按钮"""
        self.driver.find_element_by_xpath("//*[@id='account']").click()
        time.sleep(2)

    def click_close_jst(self):
        self.b.time2()
        """点击关闭结算窗口按钮"""
        self.driver.find_element_by_xpath("//*[@class='close_js']").click()
        time.sleep(2)

    def click_saveMonery2(self):
        self.b.time2()
        """点击免一元零头按钮"""
        self.driver.find_element_by_xpath("//*[@id='saveMonery2']").click()
        time.sleep(2)

    def click_saveMonery1(self):
        self.b.time2()
        """点击免十元内零头按钮"""
        self.driver.find_element_by_xpath("//*[@id='saveMonery1']").click()
        time.sleep(2)

    def click_xiaoyu(self):
        self.b.time2()
        """点击付款金额小于实际金额确定按钮"""
        self.driver.find_element_by_xpath("//*[@class='dialogFoodButton dialogSureButton dialogRedButton']").click()
        time.sleep(2)

    def input_payM(self, payM):
        self.b.time2()
        """结算窗口输入实收金额"""
        self.driver.find_element_by_xpath("//*[@id='payM']").clear()
        self.driver.find_element_by_xpath("//*[@id='payM']").send_keys(payM)

    def input_payN(self, payN):
        self.b.time2()
        """结算窗口输入实收金额"""
        self.driver.find_element_by_xpath("//*[@id='payM']").clear()
        self.driver.find_element_by_xpath("//*[@id='payM']").send_keys(payN)


    def click_payTypeButton(self):
        self.b.time2()
        """点击扫码按钮"""
        self.driver.find_element_by_xpath("//*[@class='pay-type-button']").click()
        time.sleep(2)

    def click_payTypeIconTip(self):
        self.b.time2()
        """点击什么是扫码问号按钮"""
        self.driver.find_element_by_xpath("//*[@class='pay-type-icon-tip']").click()
        time.sleep(2)

    def click_qrBtn(self):
        self.b.time2()
        """点击扫码支付页面支付码按钮"""
        self.driver.find_element_by_xpath("//*[@id='qrBtn']").click()
        time.sleep(2)

    def click_dialogFoodButton(self):
        self.b.time2()
        """点击返回现金支付按钮"""
        self.driver.find_element_by_xpath("//*[@id='dialogFoodButton dialogCancelButton dialogWhiteButton']").click()
        time.sleep(2)

    def click_dialogSureButton(self):
        self.b.time2()
        """点击返回扫码支付按钮"""
        self.driver.find_element_by_xpath("//*[@id='dialogFoodButton dialogSureButton dialogRedButton']").click()
        time.sleep(2)

    def click_yEs(self):
        self.b.time2()
        """点击确认按钮"""
        self.driver.find_element_by_xpath("//*[@id='yEs']").click()
        time.sleep(2)

    def click_notPrint(self):
        self.b.time2()
        """点击不打印小票结算"""
        self.driver.find_element_by_xpath("//*[@id='notPrint']").click()
        time.sleep(2)

    def click_lastCountUl(self):
        self.b.time2()
        """点击继续销售"""
        self.driver.find_element_by_xpath("//*[@class='last_AccountS']/button").click()
        time.sleep(2)

    def click_delete(self):
        self.b.time2()
        """点击删除按钮"""
        self.driver.find_element_by_xpath("//*[@class='l6 delete']").click()

    def click_dialogRedButton(self):
        self.b.time2()
        """点击删除后确定按钮"""
        self.driver.find_element_by_xpath("//*[@class='dialogBox ']/tbody/tr[3]/td[1]/a[2]").click()

    def click_dialogWhiteButton(self):
        self.b.time2()
        """点击删除后点击取消"""
        self.driver.find_element_by_xpath("//*[@class='dialogBox ']/tbody/tr[3]/td[1]/a[1]").click()

    def click_danjia(self, danjia):
        """修改商品单价"""
        self.b.time2()
        autoit.mouse_click("left", 594, 262, 1)
        self.b.time3()
        self.driver.find_element_by_xpath("//*[@class='l3 pirce cart-col flex-center']").send_keys(danjia)

    def input_count(self, count):
        self.b.time2()
        """修改商品数量"""
        autoit.mouse_click("left", 750, 262, 1)
        self.b.time2()
        autoit.send(count)

    def input_money(self, money):
        self.b.time2()
        """修改商品金额"""
        autoit.mouse_click("left", 930, 260, 1)
        self.b.time3()
        autoit.send(money)

    def input_goodsNameInput(self, goodsNameInput):
        self.b.time2()
        """输入未入库商品名称"""
        for i in goodsNameInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='goodsNameInput']").send_keys(i)

    def input_salePriceInput(self, salePriceInput):
        self.b.time2()
        """输入未入库商品销售价格"""
        for i in salePriceInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='salePriceInput']").send_keys(i)

    def input_saleVipInput(self, saleVipInput):
        self.b.time2()
        """输入未入库商品会员价格"""
        for i in saleVipInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='saleVipInput']").send_keys(i)

    def input_purchasePriceInput(self, purchasePriceInput):
        self.b.time2()
        """输入未入库商品进货价格"""
        for i in purchasePriceInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='purchasePriceInput']").send_keys(i)

    def input_purchaseNumInput(self, purchaseNumInput):
        self.b.time2()
        """输入未入库商品进货数量"""
        for i in purchaseNumInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='purchaseNumInput']").send_keys(i)

    def click_icon(self,):
        self.b.time2()
        """点击单位下拉框"""
        self.driver.find_element_by_xpath("//*[@class='yzg-select-input']").click()

    def click_quxiao(self):
        self.b.time2()
        """点击未入库页面取消按钮"""
        self.driver.find_element_by_xpath("//*[@class='yzg-btn yzg-btn-white fl cancel']").click()

    def excpet1(self, str1):
        driver = self.driver
        result1 = driver.find_element_by_xpath('//*[@class="payLi1"]/em').text
        print result1
        assert result1 == str1

    def excpet2(self, str2):
        driver = self.driver
        result2 = driver.find_element_by_xpath('//*[@class="payLi2"]/em').text# 获取用户名输入框的提示文本
        print result2
        assert result2 == str2

    def excpet3(self, str3):
        driver = self.driver
        result3 = driver.find_element_by_xpath('//*[@class= "payLi4"]/em').text# 获取用户名输入框的提示文本
        print result3
        assert result3 == str3

    def excpet4(self, str4):
        driver = self.driver
        result4 = driver.find_element_by_xpath('//*[@class="payLi5"]/em').text# 获取用户名输入框的提示文本
        print result4
        assert result4 == str4

    def click_space(self):
        """点击空格键"""
        self.b.time2()
        autoit.send("{SPACE}")
        self.b.time2()

    def login1(self, vip, barCode, str1, str2, str3, str4):
        """收银台正常会员结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        # self.b.time2()
        self.click_yEs()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login2(self,vip, barCode, str1,str2,str3,str4):
        """不打印小票结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login3(self, vip, barCode, str1,str2,str3,str4):
        """挂单取单销售"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_billLink()
        self.click_closequdana()
        self.click_billLink()
        self.click_qudana()
        self.click_closequdana()
        self.click_jiesuan()
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login4(self, vip, barCode, str1,str2,str3,str4):
        """免一元内零头结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.click_saveMonery2()
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login5(self, vip, barCode,str1,str2,str3,str4):
        """免十元内零头"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.click_saveMonery1()
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login6(self, vip, barCode, payM, str1, str2, str3, str4):
        """赊账结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.input_payM(payM)
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login7(self, vip, barCode, payM, str1,str2,str3,str4):
        """十元内零头减免加赊账结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.click_saveMonery1()
        self.input_payM(payM)
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login8(self, vip, barCode, payM, str1, str2, str3, str4):
        """一元内零头减免加赊账结算"""
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_jiesuan()
        self.click_jiesuan()
        self.click_saveMonery2()
        self.input_payM(payM)
        self.click_notPrint()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

if __name__ == "__main__":
    a = shyt()
    a.open_uzg("9999999905", "999905")
    a.b.time2()
    a.click_shyt()
    a.b.time2()
    a.input_shytiframe()
    #a.login8("12","5","50","￥12.00元 ￥0.00元 ￥50.00元 ￥38.00元")
    #a.login5("123456", "12", "￥12.00元 ￥0.00元 ￥12.00元 ￥0.00元")
    #a.input_barCode(12)
    #a.click_jiesuan()
    #a.input_pirce(13)
    #a.login6("123456", "12", "5", "￥12.00元 ￥2.00元 ￥5.00元 ￥5.00元")
    #a.login2("9999999905", "999905",  "59555", "789", "12", "11", "10", "9", "pinggup")
    #a.click_billLink()
    #a.click_closequdana()
    #a.click_qudana()
    #a.click_billdela()
    #a.index_uzg()
    #a.click_account()
