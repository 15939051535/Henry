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
        self.b.is_iframe("shprk")

    def stroage_pack(self):
        '''切换到商品入库—包装商品的iframe上'''
        self.b.is_iframe("iframe0")

    def stroage_inbulk(self):
        '''切换到商品入库—散货商品的iframe上'''
        self.b.is_iframe("iframe1")

    def storage_free(self):
        '''释放iframe'''
        self.driver.switch_to.default_content()

    '''散货商品散货库、销售中、入库记录定位'''
    def click_inbulk(self):
        """点击散货库按钮，点击左侧散货大类散装零食"""
        self.t.time2()
        autoit.mouse_click("left", 454, 162, 1)
        self.t.time2()
        autoit.mouse_click("left", 102, 270, 1)

    def click_onsale(self):
        """点击销售中按钮，点击左侧散货大类散装零食"""
        self.t.time2()
        autoit.mouse_click("left", 575, 164, 1)
        self.t.time2()
        autoit.mouse_click("left", 102, 270, 1)

    def click_record(self):
        """点击入库记录"""
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

    def click_newstorage(self):
        '''点击新建散货按钮，弹出新建散货页面'''
        self.t.time2()
        autoit.mouse_click("left", 1370, 210, 1)

    def click_putaway(self):
        """点击上架入库(散货库—散装零食—混称饼干(第一个商品))"""
        self.t.time2()
        autoit.mouse_click("left", 850, 285, 1)

    def click_edit(self):
        '''点击销售中按钮，选中刚才上架入库散货的编辑按钮，进入散货编辑页面'''
        self.t.time2()
        autoit.mouse_click("left", 872, 263, 1)

    '''散货入库输入框定位'''
    def input_name(self, itemname):
        '''输入商品名称'''
        self.t.time2()
        loc = ("xpath", "//*[@id='goodsNameInput']")
        self.b.clear_keys(loc)
        for i in itemname:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_sale(self, saleprice):
        """输入销售单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='salePriceInput']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_vip(self, vipprice):
        """输入会员价格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='vipPriceInput']")
        self.b.clear_keys(loc)
        for i in vipprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purprice(self, purprice):
        """输入进货单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        self.b.clear_keys(loc)
        for i in purprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum(self, purnum):
        """输入进货数量"""
        self.t.time2()
        loc = ("xpath", "//*[@id='stockInput']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_standard(self, standard):
        """输入商品规格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='standardInput']")
        self.b.clear_keys(loc)
        for i in standard:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def click_supplier(self):
        """点击供应商并选择供应商"""
        self.t.time2()
        autoit.mouse_click("left", 1393, 538, 1)
        self.t.time2()
        autoit.mouse_click("left", 1241, 623, 1)

    def click_arrow(self):
        """点击商品单位(下拉框)，选择商品单位'斤'"""
        self.t.time2()
        autoit.mouse_click("left", 1200, 610, 1)
        self.t.time2()
        autoit.mouse_click("left", 1030, 668, 1)

    def contrast_result1(self, result):
        """新建散货—断言散货名称输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@id='goodsNameInput']")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result
        # try:
        #     assert itemname == result
        #     print ('Test pass.')
        # except Exception as e:
        #     print ("Test fail.", format(e))

    def contrast_result2(self, result):
        """新建散货—断言销售价格输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@id='salePriceInput']")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def contrast_result3(self, result):
        """新建散货—断言进货价格输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@id='purchasePriceInput']")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def contrast_result4(self, result):
        """新建散货—断言散货商品单位文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@id='standardUnitInput']")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    '''已上架散货入库输入框定位'''
    def storage_button(self):
        """点击销售中的入库按钮(销售中已上架的散货商品入库—散装零食的第一个商品)"""
        self.t.time2()
        autoit.mouse_click("left", 856, 314, 1)

    def input_purprice1(self, saleprice):
        """输入进货价格"""
        self.t.time2()
        loc = ("xpath", "//*[@name='salePriceInput']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum1(self, purnum):
        """输入进货数量"""
        self.t.time2()
        loc = ("xpath", "//*[@name='stock']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def click_supplier1(self):
        """点击供应商并选择供应商"""
        self.t.time2()
        autoit.mouse_click("left", 925, 427, 1)
        self.t.time2()
        autoit.mouse_click("left", 749, 638, 1)

    def contrast_result5(self, result):
        """已上架商品入库—断言进货价格输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@class='dialogBox ']/tbody/tr[2]/td/div/div/div/div/div[2]/input")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def contrast_result6(self, result):
        """已上架商品入库—断言进货数量输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@class='dialogBox ']/tbody/tr[2]/td/div/div/div/div[2]/div[2]/input")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def record_edit(self):
        """点击入库记录中第一个商品的编辑按钮"""
        self.t.time2()
        autoit.mouse_click("left", 1374, 250, 1)

    def input_purprice2(self, saleprice):
        """输入进货价格"""
        self.t.time2()
        loc = ("xpath", "//*[@name='price']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum2(self, purnum):
        """输入进货数量"""
        self.t.time2()
        loc = ("xpath", "//*[@name='count']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def contrast_result7(self, result):
        """入库记录编辑—断言进货价格输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@class='dialogBox ']/tbody/tr[2]/td/div/label[1]/div/input")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def contrast_result8(self, result):
        """入库记录编辑—断言进货数量输入框文本与预期结果"""
        value = ("placeholder")
        loc = ("xpath", "//*[@class='dialogBox ']/tbody/tr[2]/td/div/label[2]/div/input")
        loc = self.b.get_text1(loc, value)
        print loc
        assert loc == result

    def contrast_result9(self, result):
        """获取第一条入库记录的商品名称与预期结果比较"""
        # value = ("placeholder")
        loc = ("xpath", "//*[@class ='dialogTipText']")
        loc = self.b.get_text(loc)
        print loc
        assert loc == result

    def contrast_result10(self, result):
        """获取第一条入库记录的商品名称与预期结果比较"""
        # value = ("placeholder")
        loc = ("xpath", "//*[@class ='rkjl-body yzg-scrollbar']/div[1]/span[2]")
        loc = self.b.get_text(loc)
        print loc
        assert loc == result

    def contrast_result11(self, result):
        """获取第一条入库记录的商品进货价格与预期结果比较"""
        # value = ("placeholder")
        loc = ("xpath", "//*[@class ='rkjl-body yzg-scrollbar']/div[1]/span[5]")
        loc = self.b.get_text(loc)
        print loc
        assert loc == result

    def storage1(self, itemname, saleprice, vipprice, purprice, purnum, standard, result):
        '''新建散货—商品名称输入框测试'''
        self.click_inbulk()
        self.click_newstorage()
        self.input_name(itemname)
        # self.input_sale(saleprice)
        # self.input_vip(vipprice)
        # self.input_purprice(purprice)
        # self.input_purnum(purnum)
        # self.input_standard(standard)
        # self.click_supplier()
        # self.click_arrow()
        self.click_enter()
        self.contrast_result1(result)
        # self.click_esc()

    def storage2(self, itemname, saleprice, vipprice, purprice, purnum, standard, result):
        '''新建散货—销售价格输入框测试'''
        self.click_inbulk()
        self.click_newstorage()
        self.input_name(itemname)
        self.input_sale(saleprice)
        # self.input_vip(vipprice)
        # self.input_purprice(purprice)
        # self.input_purnum(purnum)
        # self.input_standard(standard)
        # self.click_supplier()
        # self.click_arrow()
        self.click_enter()
        self.contrast_result2(result)
        # self.click_esc()

    def storage3(self, itemname, saleprice, vipprice, purprice, purnum, standard, result):
        '''新建散货—进货价格输入框测试'''
        self.click_inbulk()
        self.click_newstorage()
        self.input_name(itemname)
        self.input_sale(saleprice)
        self.input_vip(vipprice)
        self.input_purprice(purprice)
        self.input_purnum(purnum)
        # self.input_standard(standard)
        # self.click_supplier()
        self.click_arrow()
        self.click_enter()
        self.contrast_result3(result)
        # self.click_esc()

    def storage4(self, itemname, saleprice, vipprice, purprice, purnum, standard, result):
        '''新建散货—商品单位输入框测试'''
        self.click_inbulk()
        self.click_newstorage()
        self.input_name(itemname)
        self.input_sale(saleprice)
        # self.input_vip(vipprice)
        # self.input_purprice(purprice)
        # self.input_purnum(purnum)
        # self.input_standard(standard)
        # self.click_supplier()
        # self.click_arrow()
        self.click_enter()
        self.contrast_result4(result)
        # self.click_esc()

    def storage5(self, saleprice, vipprice, purprice, purnum, standard, result):
        '''上架入库—销售价格输入框测试'''
        self.click_onsale()
        self.click_putaway()
        self.input_sale(saleprice)
        self.input_vip(vipprice)
        self.input_purprice(purprice)
        self.input_purnum(purnum)
        self.input_standard(standard)
        self.click_supplier()
        self.click_arrow()
        self.click_enter()
        self.contrast_result2(result)
        self.click_esc()

    def storage6(self, saleprice, vipprice, purprice, purnum, standard, result):
        '''上架入库—进货价格输入框测试'''
        self.click_onsale()
        self.click_putaway()
        self.input_sale(saleprice)
        self.input_vip(vipprice)
        self.input_purprice(purprice)
        self.input_purnum(purnum)
        self.input_standard(standard)
        self.click_supplier()
        self.click_arrow()
        self.click_enter()
        self.contrast_result3(result)
        self.click_esc()

    def storage7(self, itemname, saleprice, vipprice, standard, result):
        '''编辑散货—商品名称输入框测试'''
        self.click_onsale()
        self.click_edit()
        self.input_name(itemname)
        self.input_sale(saleprice)
        self.input_vip(vipprice)
        self.input_standard(standard)
        self.click_supplier()
        self.click_arrow()
        self.click_enter()
        self.contrast_result1(result)

    def storage8(self, itemname, saleprice, vipprice, standard, result):
        '''编辑散货—销售价格输入框测试'''
        self.click_onsale()
        self.click_edit()
        self.input_name(itemname)
        self.input_sale(saleprice)
        self.input_vip(vipprice)
        self.input_standard(standard)
        self.click_supplier()
        self.click_arrow()
        self.click_enter()
        self.contrast_result2(result)

    def storage9(self, saleprice, purnum, result):
        '''销售中—入库—进货价格输入框测试'''
        self.click_onsale()
        self.storage_button()
        self.input_purprice1(saleprice)
        self.input_purnum1(purnum)
        self.click_supplier1()
        self.click_enter()
        self.contrast_result5(result)

    def storage10(self, saleprice, purnum, result):
        '''销售中—入库—进货数量输入框测试'''
        self.click_onsale()
        self.storage_button()
        self.input_purprice1(saleprice)
        self.input_purnum1(purnum)
        self.click_supplier1()
        self.click_enter()
        self.contrast_result6(result)

    def storage11(self, saleprice, purnum, result):
        '''入库记录—编辑—进货价格输入框测试'''
        self.click_onsale()
        self.record_edit()
        self.input_purprice2(saleprice)
        self.input_purnum2(purnum)
        self.click_enter()
        self.contrast_result7(result)

    def storage12(self, saleprice, purnum, result):
        '''入库记录—编辑—进货价格输入框测试'''
        self.click_onsale()
        self.record_edit()
        self.input_purprice2(saleprice)
        self.input_purnum2(purnum)
        self.click_enter()
        self.contrast_result8(result)

    def storage13(self, result):
        '''新建、上架、编辑散货成功后，在入库记录的第一条记录中验证，验证商品名称'''
        self.click_onsale()
        self.record_edit()
        self.contrast_result10(result)

    def storage14(self, result):
        '''入库，编辑(入库记录)成功后，在入库记录的第一条记录中验证，验证进货价格'''
        self.click_onsale()
        self.record_edit()
        self.contrast_result11(result)


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
    a.storage1('ceshi', '', '10', '10', '10', '10', u'销售价格不能为空')
