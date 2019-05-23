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
        """点击商品管理—商品入库，进入商品入库页面"""
        self.t.time2()
        autoit.mouse_click("left", 739, 24, 1)
        self.t.time2()
        autoit.mouse_click("left", 726, 50, 1)

    def stay_storage(self):
        '''刷新商品入库页面'''
        self.driver.get(storage_url)

    def storage_iframe(self):
        '''切换到商品入库的iframe上'''
        loc = ("id", "shprk")
        self.b.switch_iframe(loc)

    def stroage_pack(self):
        '''切换到商品入库—包装商品的iframe上'''
        loc = ("id", "iframe0")
        self.b.switch_iframe(loc)

    def storage_free(self):
        '''释放iframe'''
        self.driver.switch_to.default_content()


    def input_code(self, itemcode):
        """输入商品编码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='ItemCode']")
        self.b.clear_keys(loc)
        for i in itemcode:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_name(self, itemname):
        """输入商品名称"""
        self.t.time2()
        loc = ("xpath", "//*[@id='ItemName']")
        self.b.clear_keys(loc)
        for i in itemname:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_sale(self, saleprice):
        """输入销售单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='SalePrice']")
        self.b.clear_keys(loc)
        for i in saleprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_vip(self, vipprice):
        """输入会员价格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='VipPrice']")
        self.b.clear_keys(loc)
        for i in vipprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_pur(self, purprice):
        """输入进货单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='PurPrice']")
        self.b.clear_keys(loc)
        for i in purprice:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_purnum(self, purnum):
        """输入进货数量"""
        self.t.time2()
        loc = ("xpath", "//*[@id='PurNum']")
        self.b.clear_keys(loc)
        for i in purnum:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_expirydate(self, expirydate):
        """输入商品保质期"""
        self.t.time2()
        loc = ("xpath", "//*[@id='expiryDate']")
        self.b.clear_keys(loc)
        for i in expirydate:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_standard(self, standard):
        """输入商品规格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='Standard']")
        self.b.clear_keys(loc)
        for i in standard:
            self.t.time3()
            self.b.send_keys1(loc, i)

    def input_marks(self, marks):
        """输入商品备注"""
        self.t.time2()
        loc = ("xpath", "//*[@id='Marks']")
        self.b.clear_keys(loc)
        for i in marks:
            self.t.time3()
            self.b.send_keys1(loc, i)

    # def click_szsp(self):
    #     """点击—商品类型—散装商品(单选按钮)"""
    #     self.t.time2()
    #     autoit.mouse_click("left", 188, 235, 1)

    def click_arrow(self):
        """点击商品单位(下拉框)，选择商品单位"""
        self.t.time2()
        autoit.mouse_click("left", 427, 272, 1)
        self.t.time2()
        autoit.mouse_click("left", 127, 424, 1)

    def click_date(self):
        """点击商品生产日期，选择本月一号的日期"""
        self.t.time2()
        autoit.mouse_click("left", 427, 307, 1)
        self.t.time2()
        autoit.mouse_click("left", 305, 404, 1)

    """关于保质期的autoit键鼠操作"""
    def click_expirydate(self):
        """点击保质期按钮"""
        self.t.time2()
        autoit.mouse_click("left", 872, 311, 1)

    def click_day(self):
        """选择天"""
        self.t.time2()
        autoit.mouse_click("left", 845, 338, 1)

    def click_month(self):
        """选择月"""
        self.t.time2()
        autoit.mouse_click("left", 845, 367, 1)

    def click_(self):
        """选择年"""
        self.t.time2()
        autoit.mouse_click("left", 845, 400, 1)

    """关于供应商的autoit键鼠操作"""
    def click_supplier(self):
        """点击供应商"""
        self.t.time2()
        autoit.mouse_click("left", 1319, 165, 1)

    def choice_supplier(self):
        """选择邮政供货"""
        self.t.time2()
        autoit.mouse_click("left", 1020, 255, 1)

    def delete_supplier(self):
        """删除供应商"""
        self.t.time2()
        autoit.mouse_click("left", 1290, 283, 1)

    def rename_supplier(self):
        """修改供应商"""
        self.t.time2()
        autoit.mouse_click("left", 1259, 284, 1)

    def input_supplier(self, editIpt):
        """修改供应商名称"""
        self.t.time2()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").clear()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").send_keys(editIpt)

    """关于商品大类的autoit键鼠操作"""
    def click_sort(self):
        """点击分类"""
        self.t.time2()
        autoit.mouse_click("left", 1323, 240, 1)

    def click_newsort(self):
        """点击新建大类"""
        self.t.time2()
        autoit.mouse_click("left", 1102, 297, 1)

    def choice_sort(self):
        """选择第一个商品大类"""
        self.t.time2()
        autoit.mouse_click("left", 1025, 320, 1)

    def delete_sort(self):
        """点击删除商品大类"""
        self.t.time2()
        autoit.mouse_click("left", 1291, 360, 1)

    def rename_sort(self):
        """点击修改商品大类"""
        self.t.time2()
        autoit.mouse_click("left", 1262, 360, 1)

    def input_sort(self, editIpt):
        """输入新建或者修改商品大类名称"""
        self.t.time2()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").clear()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").send_keys(editIpt)

    """关于入库、保存、重置功能的autoit键鼠操作"""
    def click_storagebutton(self):
        """点击入库按钮"""
        self.t.time2()
        autoit.mouse_click("left", 88, 346, 1)

    def click_savebutton(self):
        """点击保存按钮"""
        self.t.time2()
        autoit.mouse_click("left", 208, 348, 1)

    def click_resetbutton(self):
        """点击重置"""
        self.t.time2()
        autoit.mouse_click("left", 329, 350, 1)

    """查看入库记录的相关键鼠操作"""
    def click_jin(self):
        """点击今日按钮"""
        self.t.time2()
        autoit.mouse_click("left", 410, 390, 1)

    def click_ben(self):
        """点击本月按钮"""
        self.t.time2()
        autoit.mouse_click("left", 547, 390, 1)

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

if __name__ == "__main__":
    a = StorageUZG()
    a.open_uzg()
    time.sleep(3)
    a.login_uzg()
    time.sleep(3)
    a.click_storage()
    a.storage_iframe()
    a.stroage_pack()
    time.sleep(3)

