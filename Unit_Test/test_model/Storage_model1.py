#coding=utf-8

from selenium import webdriver
import time
from test_base import base_pack
from test_common import Wait_Time
import autoit


APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe')  #定义邮掌柜路径
storage_url = ("C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\face\\_modules_\\storage\\packaged\\packaged.html")#定义商品入库页面file文件路径

options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class StorageUZG(object):

    t = Wait_Time.Ttime()

    def open_uzg(self):
        '''打开邮掌柜'''
        self.driver = webdriver.Chrome(chrome_options=options)
        self.b = base_pack.BasePage(self.driver)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def login_uzg(self, usr="wanghengli", pwd="hengli"):
        """登录邮掌柜"""
        self.t.time2()
        login_button = ("xpath", "//*[@id='loginBtn']")
        username = ("xpath", "//*[@id='username']")
        password = ("xpath", "//*[@id='password']")
        self.b.clear_keys(username)
        for i in usr:
            self.t.time3()
            self.b.send_keys1(username, i)
        self.t.time2()
        self.b.clear_keys(password)
        for i in pwd:
            self.t.time3()
            self.b.send_keys1(password, i)
        self.b.click(login_button)

    def click_storage(self):
        """点击商品管理—商品入库—散装商品，进入散货商品入库页面"""
        self.t.time2()
        autoit.mouse_click("left", 739, 24, 1)
        self.t.time2()
        autoit.mouse_click("left", 726, 50, 1)
        self.t.time2()
        autoit.mouse_click("left", 282, 104, 1)

    def stay_storage(self):
        '''刷新商品入库页面'''
        self.driver.get(storage_url)

    def storage_iframe(self):
        '''切换到商品入库的iframe上'''
        # self.driver.switch_to_frame("shprk")
        self.b.is_iframe("shprk")
    def stroage_pack(self):
        '''切换到商品入库—包装商品的iframe上'''
        self.b.is_iframe("iframe0")
        # self.driver.switch_to_frame("iframe0")

    def stroage_inbulk(self):
        '''切换到商品入库—散货商品的iframe上'''
        # self.driver.switch_to_frame("iframe1")
        self.b.is_iframe("iframe1")

    def storage_free(self):
        '''释放iframe'''
        self.driver.switch_to.default_content()

    def click_inbulk(self):
        """点击散货库按钮，点击左侧散货大类散装零食"""
        self.t.time2()
        autoit.mouse_click("left", 454, 162, 1)
        self.t.time2()
        autoit.mouse_click("left", 102, 270, 1)

    def click_onsale(self):
        """点击销售中按钮"""
        self.t.time2()
        autoit.mouse_click("left", 575, 164, 1)
        self.t.time2()
        autoit.mouse_click("left", 102, 270, 1)

    def click_record(self):
        """点击入库记录,并选中第一条记录"""
        self.t.time2()
        autoit.mouse_click("left", 700, 164, 1)

    def click_enter(self):
        """点击enter键"""
        self.t.time2()
        autoit.send("{ENTER}")
        self.t.time2()

    def click_esc(self):
        """点击esc键"""
        self.t.time2()
        autoit.send("{ESC}")
        self.t.time2()

    '''新建散货商品的元素定位'''
    def click_newstorage(self):
        '''点击新建散货按钮，弹出新建散货页面'''
        self.t.time2()
        autoit.mouse_click("left", 1370, 210, 1)

    def input_name(self, itemname):
        '''输入商品名称(新建散货)'''
        self.t.time2()
        loc = ("xpath", "//*[@id='goodsNameInput']")
        self.b.clear_keys(loc)
        for i in itemname:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_sale(self, saleprice):
        """输入销售单价(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='salePriceInput']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_vip(self, vipprice):
        """输入会员价格(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='vipPriceInput']")
        self.b.clear_keys(loc)
        for i in vipprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_pur(self, purprice):
        """输入进货单价(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        self.b.clear_keys(loc)
        for i in purprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum(self, purnum):
        """输入进货数量(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='stockInput']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_standard(self, standard):
        """输入商品规格(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='standardInput']")
        self.b.clear_keys(loc)
        for i in standard:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def click_supplier(self):
        """点击供应商并选择邮政供货(新建散货)"""
        self.t.time2()
        autoit.mouse_click("left", 1393, 538, 1)
        self.t.time2()
        autoit.mouse_click("left", 1241, 623, 1)

    def click_arrow(self):
        """点击商品单位(下拉框)，选择商品单位'斤'(新建散货)"""
        self.t.time2()
        autoit.mouse_click("left", 1200, 610, 1)
        self.t.time2()
        autoit.mouse_click("left", 1030, 668, 1)

    def contrast_result1(self, result):
        """新建散货—断言散货名称输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@id='goodsNameInput']")
        itemname = self.b.get_text1(loc, value)
        print itemname
        # assert itemname == result
        try:
            assert itemname == result
            print ('Test pass.')
        except Exception as e:
            print ("Test fail.", format(e))

    def contrast_result2(self, result):
        """新建散货—断言销售价格输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='salePriceInput']")
        saleprice = self.b.get_text(loc)
        print saleprice
        assert saleprice == result

    def contrast_result3(self, result):
        """新建散货—断言进货价格输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        purprice = self.b.get_text(loc)
        print purprice
        assert purprice == result

    def contrast_result4(self, result):
        """新建散货—断言散货商品单位文本与预期结果"""
        loc = ("xpath", "//*[@id='standardUnitInput']")
        unit = self.b.get_text(loc)
        print unit
        assert unit == result

    """散货商品上架入库的元素定位"""
    def click_putaway(self):
        """点击上架入库(混称饼干)"""
        self.t.time2()
        autoit.mouse_click("left", 850, 285, 1)

    def input_sale1(self, saleprice):
        """输入商品销售价格(上架入库)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='salePriceInput']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_vip1(self, vipprice):
        """输入会员价格(上架入库)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='salePriceInput']")
        self.b.clear_keys(loc)
        for i in vipprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_pur1(self, purprice):
        """输入进货价格(上架入库)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        self.b.clear_keys(loc)
        for i in purprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum1(self, purnum):
        """输入进货数量(上架入库)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='stockInput']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_standard1(self, standard):
        """输入商品规格(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='standardInput']")
        self.b.clear_keys(loc)
        for i in standard:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def click_supplier1(self):
        """点击供应商并选择邮政供货(新建散货)"""
        self.t.time2()
        autoit.mouse_click("left", 1393, 538, 1)
        self.t.time2()
        autoit.mouse_click("left", 1241, 623, 1)

    def contrast_result5(self, result):
        """新建散货—断言销售价格输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='salePriceInput']")
        saleprice = self.b.get_text(loc)
        print saleprice
        assert saleprice == result

    def contrast_result6(self, result):
        """新建散货—断言进货价格输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        purprice = self.b.get_text(loc)
        print purprice
        assert purprice == result

    """散货编辑的元素定位"""
    def click_edit(self):
        '''点击销售中按钮，选中刚才上架入库散货的编辑按钮，进入散货编辑页面'''
        self.t.time2()
        autoit.mouse_click("left", 872, 263, 1)

    def input_name2(self, itemname):
        '''输入商品名称(编辑散货)'''
        self.t.time2()
        loc = ("xpath", "//*[@id='goodsNameInput']")
        self.b.clear_keys(loc)
        for i in itemname:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_sale2(self, saleprice):
        """输入销售价格(编辑散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='salePriceInput']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_vip2(self, vipprice):
        """输入会员价格(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='vipPriceInput']")
        self.b.clear_keys(loc)
        for i in vipprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_standard2(self, standard):
        """输入商品规格(新建散货)"""
        self.t.time2()
        loc = ("xpath", "//*[@id='standardInput']")
        self.b.clear_keys(loc)
        for i in standard:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def click_supplier2(self):
        """点击供应商并选择邮政供货(新建散货)"""
        self.t.time2()
        autoit.mouse_click("left", 1393, 538, 1)
        self.t.time2()
        autoit.mouse_click("left", 1241, 623, 1)

    def click_arrow2(self):
        """点击商品单位(下拉框)，选择商品单位'斤'(新建散货)"""
        self.t.time2()
        autoit.mouse_click("left", 1200, 610, 1)
        self.t.time2()
        autoit.mouse_click("left", 1030, 668, 1)

    def contrast_result7(self, result):
        """新建散货—断言散货名称输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='goodsNameInput']")
        itemname = self.b.get_text(loc)
        print itemname
        assert itemname == result

    def contrast_result8(self, result):
        """新建散货—断言销售价格输入框文本与预期结果"""
        loc = ("xpath", "//*[@id='salePriceInput']")
        saleprice = self.b.get_text(loc)
        print saleprice
        assert saleprice == result


if __name__ == "__main__":
    a = StorageUZG()
    a.open_uzg()
    time.sleep(3)
    a.login_uzg()
    time.sleep(10)
    a.click_storage()
    a.storage_iframe()
    a.stroage_inbulk()
    time.sleep(3)
    a.click_inbulk()
    time.sleep(2)
    a.click_newstorage()
    time.sleep(2)
    a.click_enter()
    time.sleep(2)
    a.contrast_result1(u"散货名称不能为空")
    time.sleep(2)
    a.quit_uzg()