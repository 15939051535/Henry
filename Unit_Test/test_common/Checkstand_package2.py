#coding=utf-8

from selenium import webdriver
import time
import Wait_Time
import autoit


APPLICATION_PATH = 'C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe'  # 定义邮掌柜路径
options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class right(object):

    b = Wait_Time.Ttime()

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def input_shytiframe(self):
        '''切换到收银台的iframe上'''
        self.driver.switch_to.frame("shyt")

    def input_hyjftiframe(self):
        '''切换到收银台的iframe上'''
        self.driver.switch_to.frame("hyjf")

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

    def click_shyt(self):
        """点击收银台"""
        self.b.time2()
        autoit.mouse_click("left", 172, 23, 1)

    def input_vip(self, vip):
        self.b.time2()
        """输入会员号码"""
        self.driver.find_element_by_xpath("//*[@id='vIp']").clear()
        self.driver.find_element_by_xpath("//*[@id='vIp']").send_keys(vip)

    def input_barCode(self, barCode):
        self.b.time2()
        """输入商品编码"""
        self.driver.find_element_by_xpath("//*[@id='barCode']").clear()
        #for i in barCode:
            #self.b.time3()
        self.driver.find_element_by_xpath("//*[@id='barCode']").send_keys(barCode)

    def click_sect(self):
        """点击散货热卖"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='散货热卖']").click()

    def click_addGoodS(self):
        """选择热卖商品"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='sPic newsanhuo-bg-c2 ']").click()

    def click_hot1(self):
        """点击热卖商品1"""
        autoit.mouse_click("left", 1200, 486, 1)

    def click_hot2(self):
        """点击热卖商品2"""
        autoit.mouse_click("left", 1287, 486, 1)

    def click_hot3(self):
        """点击热卖商品3"""
        autoit.mouse_click("left", 1367, 486, 1)

    def click_hot4(self):
        """点击热卖商品4"""
        autoit.mouse_click("left", 1207, 562, 1)

    def click_hot5(self):
        """点击热卖商品5"""
        autoit.mouse_click("left", 1293, 562, 1)

    def click_hot6(self):
        """点击热卖商品6"""
        autoit.mouse_click("left", 1371, 562, 1)

    def click_hot7(self):
        """点击热卖商品7"""
        autoit.mouse_click("left", 1201, 650, 1)

    def click_hot8(self):
        """点击热卖商品8"""
        autoit.mouse_click("left", 1295, 650, 1)

    def click_hot9(self):
        """点击热卖商品9"""
        autoit.mouse_click("left", 1377, 650, 1)


    def input_unPackedSaleNum(self, unPackedSaleNum):
        self.b.time2()
        """修改热卖商品销售数量"""
        self.driver.find_element_by_xpath("//*[@id='unPackedSaleNum']").clear()
        self.driver.find_element_by_xpath("//*[@id='unPackedSaleNum']").send_keys(unPackedSaleNum)

    def input_unPackedSaleCount(self, unPackedSaleCount):
        self.b.time2()
        """修改热卖商品销售金额"""
        self.driver.find_element_by_xpath("//*[@id='unPackedSaleCount']").clear()
        self.driver.find_element_by_xpath("//*[@id='unPackedSaleCount']").send_keys(unPackedSaleCount)

    def click_yesBTN(self):
        """点击热卖散货销售确定按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='yesBTN']").click()

    def click_xxClose(self):
        """点击热卖散货销售差号按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='xxClose']").click()

    def click_ssan(self):
        """点击散货销售搜索按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='change-btn btn']").click()

    def input_newsanhuoSearchInput(self, newsanhuoSearchInput):
        self.b.time2()
        """搜索散货商品"""
        self.driver.find_element_by_xpath("//*[@id='newsanhuoSearchInput']").clear()
        for i in newsanhuoSearchInput:
            self.b.time3()
            self.driver.find_element_by_xpath("//*[@id='newsanhuoSearchInput']").send_keys(i)

    def click_shss(self):
        """输入散货商品后点击搜索按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='search-btn btn']").click()

    def click_gotosanhuo(self):
        """输入散货商品后点击搜索按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='goto-sanhuo-btn yzg-btn']").click()

    def click_chang(self):
        """点击常用商品"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='常用']").click()

    def click_shc(self):
        """点击水产商品"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='水产']").click()

    def click_hot(self):
        """点击热食即食"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='热食即食']").click()

    def click_xxsg(self):
        """点击新鲜水果"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='新鲜水果']").click()

    def click_rou(self):
        """点击肉禽"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='肉禽']").click()

    def click_san(self):
        """点击散装零食"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='散装零食']").click()

    def click_jclw(self):
        """点击酱菜卤味"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='酱菜卤味']").click()

    def click_lytw(self):
        """点击粮油调味"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='粮油调味']").click()

    def click_nan(self):
        """点击南北干货"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='南北干货']").click()

    def click_shucai(self):
        """点击蔬菜蛋菇"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[text()='蔬菜蛋菇']").click()

    def click_goods(self):
        """选择商品"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='goods-list goods-list-1']/span[2]").click()

    def click_tjBatchChange(self):
        """点击换一批"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@id='tjBatchChange']").click()
        time.sleep(2)

    def click_mask(self):
        """点击待售商品"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='goods-list goods-list-2']/span[1]").click()
        time.sleep(2)

    def click_close(self):
        """点击关闭按钮"""
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@class='yzg-side-box-btn-close close']").click()
        time.sleep(2)

    def input_salePrice(self, salePrice):
        self.b.time2()
        """输入散货商品销售价格"""
        self.driver.find_element_by_xpath("//*[@id='salePriceInput']").send_keys(salePrice)

    def input_saleNum(self, saleNum):
        self.b.time2()
        """输入散货商品销售数量"""
        self.driver.find_element_by_xpath("//*[@id='saleNum']").send_keys(saleNum)

    def input_purchasePriceInput(self, purchasePriceInput):
        self.b.time2()
        """输入散货商品进货价格"""
        self.driver.find_element_by_xpath("//*[@id='purchasePriceInput']").send_keys(purchasePriceInput)

    def input_purchaseNumInput(self, purchaseNumInput):
        self.b.time2()
        """输入散货商品进货数量"""
        self.driver.find_element_by_xpath("//*[@id='purchaseNumInput']").send_keys(purchaseNumInput)

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

    def click_account(self):
        self.b.time2()
        """点击结算按钮"""
        self.driver.find_element_by_xpath("//*[@id='account']").click()
        time.sleep(2)

    def click_account1(self):
        self.b.time2()
        """点击关闭结算窗口按钮"""
        self.driver.find_element_by_xpath("//*[@id='account']").click()
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

    def input_payM(self, payM):
        self.b.time2()
        self.driver.find_element_by_xpath("//*[@id='payM']").send_keys(payM)

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

    def click_xycf(self):
        self.b.time2()
        """点击确认按钮（付款金额小于应付金额窗口）"""
        self.driver.find_element_by_xpath("//*[@class='dialogFoodButton dialogSureButton dialogRedButton']").click()
        time.sleep(2)

    def click_lastCountUl(self):
        self.b.time2()
        """点击继续销售"""
        self.driver.find_element_by_xpath("//*[@class='last_AccountS']/button").click()
        time.sleep(2)

    def click_huiche(self):
        """点击enter键"""
        self.b.time2()
        autoit.send("{ENTER}")
        self.b.time2()

    def click_tuichu(self):
        """点击esc键"""
        self.b.time2()
        autoit.send("{ESC}")
        self.b.time2()

    def click_space(self):
        """点击空格键"""
        self.b.time2()
        autoit.send("{SPACE}")
        self.b.time2()

    def click_shopkeeper(self):
        """点击掌柜"""
        autoit.mouse_click("left", 53, 21, 1)

    def click_integral(self):
        """点击积分兑换"""
        autoit.mouse_click("left", 1360, 230, 1)

    def click_huiyuan(self):
        """点击新建会员"""
        autoit.mouse_click("left", 53, 21, 1)

    def click_one(self):
        """点击免一元零头"""
        autoit.mouse_click("left", 664, 402, 1)

    def click_ten(self):
        """点击免十元零头"""
        autoit.mouse_click("left", 831, 402, 1)

    def click_guadan(self):
        """点击挂单"""
        autoit.mouse_click("left", 1061, 813, 1)

    def click_qudan(self):
        """点击取单1"""
        autoit.mouse_click("left", 853, 692, 1)

    def click_shxs(self):
        """点击散货销售"""
        autoit.mouse_click("left", 1376, 417, 1)

    def click_spfl(self):
        """点击商品分类"""
        autoit.mouse_click("left", 1352, 260, 1)

    def click_dssp(self):
        """点击待售商品"""
        autoit.mouse_click("left", 1011, 467, 1)

    def click_danwei(self):
        """点击单位"""
        autoit.mouse_click("left", 1199, 405, 1)

    def click_xzdw(self):
        """选择单位"""
        autoit.mouse_click("left", 1092, 532, 1)

    def click_guige(self):
        """点击规格"""
        autoit.mouse_click("left", 1400, 404, 1)

    def click_xzgg(self):
        """选择规格"""
        autoit.mouse_click("left", 1348, 489, 1)

    def click_xiaoshou(self):
        """选择规格"""
        autoit.mouse_click("left", 685, 572, 1)

    def click_shortcut(self):
        """点击快捷键"""
        autoit.mouse_click("left", 1043, 127, 1)

    def excpet1(self, str1):
        driver = self.driver
        result1 = driver.find_element_by_xpath('//*[@class="payLi1"]/em').text
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result1
        assert result1 == str1

    def excpet2(self, str2):
        driver = self.driver
        result2 = driver.find_element_by_xpath('//*[@class="payLi2"]/em').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result2
        assert result2 == str2

    def excpet3(self, str3):
        driver = self.driver
        result3 = driver.find_element_by_xpath('//*[@class= "payLi4"]/em').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result3
        assert result3 == str3

    def excpet4(self, str4):
        driver = self.driver
        result4 = driver.find_element_by_xpath('//*[@class="payLi5"]/em').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result4
        assert result4 == str4

    def excpeta(self, num):
        """验证本次积分断言"""
        driver = self.driver
        result1 = driver.find_element_by_xpath('//*[@id="currentIntegralBox"]').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result1
        assert result1 == num

    def excpetb(self, num1):
        """验证积分兑换断言"""
        driver = self.driver
        result2 = driver.find_element_by_xpath('//*[@class="account"]').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result2
        assert result2 == num1

    def excpetc(self, result):
        """会员冻结跳转会员管理or商品已下架"""
        driver = self.driver
        num = driver.find_element_by_xpath('//*[@class="dialogBodyText dialogFlagWarn"]').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print num
        assert num == result

    def excpetd(self, result1):
        """验证快捷键"""
        driver = self.driver
        num = driver.find_element_by_xpath('//*[@class="dialogHeadTitle"]').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print num
        assert num == result1


    def login9(self, vip, barCode, num):
        """验证会员本次积分是否正确"""
        self.b.time2()
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_huiche()
        self.excpeta(num)
        self.click_shopkeeper()
        self.click_xiaoshou()
        self.click_shopkeeper()

    def login10(self, vip, barCode, num1):
        """验证积分兑换是否跳转"""
        self.b.time2()
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_integral()
        self.excpetb(num1)
        self.b.time2()
        self.click_shopkeeper()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_shopkeeper()

    def login11(self, vip, result):
        """会员冻结验证是否跳转会员管理"""
        self.b.time2()
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.excpetc(result)
        self.click_tuichu()

    def login12(self, vip, barCode, result):
        """验证提示商品已下架"""
        self.b.time2()
        self.input_vip(vip)
        self.input_barCode(barCode)
        self.click_huiche()
        self.b.time2()
        self.excpetc(result)
        self.click_tuichu()

    def login13(self,  result1):
        """验证快捷键跳转"""
        self.click_shortcut()
        self.b.time2()
        self.excpetd(result1)
        self.click_tuichu()

    def login14(self, vip,  barCode, str1, str2, str3, str4):
        """选择热卖商品销售"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot4()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login15(self, vip, barCode,unPackedSaleNum, str1, str2, str3, str4):
        """修改热卖商品销售数量"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot4()
        self.b.time2()
        self.input_unPackedSaleNum(unPackedSaleNum)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login16(self, vip, barCode, unPackedSaleCount, str1, str2, str3, str4):
        """修改热卖商品销售金额"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot4()
        self.b.time2()
        self.input_unPackedSaleCount(unPackedSaleCount)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login17(self, vip, barCode, unPackedSaleCount, str1, str2, str3, str4):
        """修改热卖商品销售金额挂单取单销售"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot4()
        self.b.time2()
        self.input_unPackedSaleCount(unPackedSaleCount)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_guadan()
        self.b.time2()
        self.click_qudan()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login18(self, vip, barCode, unPackedSaleCount, str1, str2, str3, str4):
        """修改热卖商品销售金额挂单取单销售免一元销售"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot4()
        self.b.time2()
        self.input_unPackedSaleCount(unPackedSaleCount)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_guadan()
        self.b.time2()
        self.click_qudan()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_one()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def login19(self, vip, barCode, unPackedSaleCount,payM, str1, str2, str3, str4):
        """修改热卖商品销售金额挂单取单销售免十元内元加修改实际金额销售"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        time.sleep(1)
        self.click_hot3()
        self.b.time2()
        self.input_unPackedSaleCount(unPackedSaleCount)
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_guadan()
        self.b.time2()
        self.click_qudan()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_ten()
        self.b.time2()
        self.input_payM(payM)
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)

    def logini(self, vip, barCode, salePrice, saleNum,purchasePriceInput, purchaseNumInput, str1, str2, str3, str4):
        """编辑新散货商品销售"""
        self.input_vip(vip)
        self.click_huiche()
        self.b.time2()
        self.input_barCode(barCode)
        self.click_huiche()
        self.click_shxs()
        self.b.time2()
        self.click_spfl()
        self.b.time2()
        self.click_mask()
        self.b.time2()
        self.input_salePrice(salePrice)
        self.b.time2()
        self.input_saleNum(saleNum)
        self.b.time2()
        self.input_purchasePriceInput(purchasePriceInput)
        self.b.time2()
        self.input_purchaseNumInput(purchaseNumInput)
        self.click_danwei()
        self.b.time2()
        self.click_xzdw()
        self.b.time2()
        self.click_guige()
        self.b.time2()
        self.click_xzgg()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.click_tuichu()
        self.b.time3()
        self.click_huiche()
        self.b.time2()
        self.click_huiche()
        self.b.time2()
        self.excpet1(str1)
        self.excpet2(str2)
        self.excpet3(str3)
        self.excpet4(str4)


if __name__ == "__main__":
    """time.sleep(3)"""
    b = right()
    b.open_uzg("9999999905", "999905")
    b.click_shyt()
    b.input_shytiframe()
    b.login13(u"快捷键<Ctrl+F5>")

    #b.click_lastCountUl()