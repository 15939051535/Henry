# coding=utf-8

from selenium import webdriver
import time
from test_base import base_pack
from test_common import Wait_Time
import autoit


APPLICATION_PATH = 'C:\\Program Files (x86)\\UleSoft\\邮掌柜5\\邮掌柜.exe'  # 定义邮掌柜路径
options = webdriver.ChromeOptions()
options.binary_location = APPLICATION_PATH


class StorageUZG(object):

    t = Wait_Time.Ttime()

    def open_uzg(self):
        """打开邮掌柜"""
        self.driver = webdriver.Chrome(chrome_options=options)
        self.b = base_pack.BasePack(self.driver)

    def quit_uzg(self):
        """退出邮掌柜"""
        self.driver.quit()

    def login_uzg(self, usr="9999999905", pwd="999905"):
        """登录邮掌柜"""
        self.t.time2()
        login_button = ("xpath", "//*[@id='loginBtn']")
        username = ("xpath", "//*[@id='username']")
        password = ("xpath", "//*[@id='password']")
        self.b.clear_keys(username)
        for i in usr:
            self.t.time1()
            self.b.send_keys1(username, i)
        self.t.time2()
        self.b.clear_keys(password)
        for i in pwd:
            self.t.time1()
            self.b.send_keys1(password, i)
        self.b.click(login_button)

    def click_storage(self):
        """点击商品管理—商品入库，进入商品入库页面"""
        self.t.time2()
        autoit.mouse_click("left", 739, 24, 1)
        self.t.time2()
        autoit.mouse_click("left", 706, 120, 1)

    def storage_iframe(self):
        """切换到商品入库的iframe上"""
        loc = ("name", "shprk")
        self.b.switch_iframe(loc)

    def stroage_pack(self):
        """切换到商品入库—包装商品的iframe上"""
        loc = ("name", "iframe0")
        self.b.switch_iframe(loc)

    def input_shpglframe(self):
        """切换到商品入库的iframe上"""
        self.driver.switch_to.frame("shprk")

    def input_shyprkframe(self):
        """切换到商品入库的iframe上"""
        self.driver.switch_to.frame("iframe0")

    def storage_free(self):
        """释放iframe"""
        self.driver.switch_to.default_content()


    def input_code(self, itemcode):
        """输入商品编码"""
        self.t.time2()
        loc = ("xpath", "//*[@id='ItemCode']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, itemcode)
        # for i in itemcode:
        #     self.t.time1()
        #     self.b.send_keys1(loc, i)

    def input_name(self, itemname):
        """输入商品名称"""
        self.t.time2()
        loc = ("xpath", "//*[@id='ItemName']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, itemname)

    def input_sale(self, saleprice):
        """输入销售单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='SalePrice']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, saleprice)

    def input_vip(self, vipprice):
        """输入会员价格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='VipPrice']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, vipprice)

    def input_pur(self, purprice):
        """输入进货单价"""
        self.t.time2()
        loc = ("xpath", "//*[@id='PurPrice']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, purprice)
        # for i in purprice:
        #     self.t.time1()
        #     self.b.send_keys1(loc, i)

    def input_purnum(self, purnum):
        """输入进货数量"""
        self.t.time2()
        loc = ("xpath", "//*[@id='PurNum']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, purnum)
        # for i in purnum:
        #     self.t.time1()
        #     self.b.send_keys1(loc, i)

    def input_expirydate(self, expirydate):
        """输入商品保质期"""
        self.t.time2()
        loc = ("xpath", "//*[@id='expiryDate']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, expirydate)


    def input_standard(self, standard):
        """输入商品规格"""
        self.t.time2()
        loc = ("xpath", "//*[@id='Standard']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, standard)


    def input_marks(self, marks):
        """输入商品备注"""
        self.t.time2()
        loc = ("xpath", "//*[@id='Marks']")
        self.b.clear_keys(loc)
        self.b.send_keys(loc, marks)

    def click_name(self):
        """点击商品名称"""
        self.t.time2()
        autoit.mouse_click("left", 147, 201, 1)


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

    def click_nian(self):
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
        autoit.mouse_click("left", 1288, 312, 1)

    def click_yes0(self):
        """是否删除供应商，点击确定"""
        self.t.time2()
        autoit.mouse_click("left", 799, 461, 1)

    def rename_supplier(self):
        """修改供应商"""
        self.t.time2()
        autoit.mouse_click("left", 1259, 313, 1)

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
        autoit.mouse_click("left", 1289, 357, 1)

    def rename_sort(self):
        """点击修改商品大类"""
        self.t.time2()
        autoit.mouse_click("left", 1257, 357, 1)

    def input_sort(self, editIpt1):
        """输入新建或者修改商品大类名称"""
        self.t.time2()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").clear()
        self.driver.find_element_by_xpath("//*[@id='editIpt']").send_keys(editIpt1)

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

    def click_delete(self):
        """点击删除按钮"""
        self.t.time2()
        autoit.mouse_click("left", 1402, 486, 1)

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

    def click_space(self):
        """点击空格键"""
        self.t.time2()
        autoit.send("{SPACE}")
        self.t.time2()



    def click_NO(self):
        """点击没有编码"""
        self.t.time2()
        autoit.mouse_click("left", 400, 161, 1)

    def click_bad(self):
        """点击空白处"""
        self.t.time2()
        autoit.mouse_click("left", 974, 321, 1)

    def excpet(self, result1):
        """验证入库是否成功or供应商名称已经存在or新增供应商成功or
        新建大类成功or修改供应商成功or此入库单对应的库存已经销售无法修改"""
        driver = self.driver
        num1 = driver.find_element_by_xpath('//*[@class="dialogBodyText dialogFlagSuccessSmall"]').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print num1
        assert num1 == result1

    def excpet1(self, result2):
        """销售单价小于进货单价断言or确定要删除吗？or是否要删除这个供应商or你确定要修改这条记录吗？"""
        driver = self.driver
        num2 = driver.find_element_by_xpath('//*[@class="dialogBodyText dialogFlagConfirmSmall"]').text
        # 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print num2
        assert num2 == result2

    def excpet4(self, num5):
        """销售单价小于进货单价断言or确定要删除吗？or是否要删除这个供应商or你确定要修改这条记录吗？"""
        driver = self.driver
        result2 = driver.find_element_by_xpath('//*[@class="dialogBox "]/table/tbody/tr/td/div[3]/span').text# 获取用户名输入框的提示文本
        # self.assertEqual(result1, str1,'断言失败')        # 断言，结果与str1(传参进来的字符串)比较
        print result2
        assert result2 == num5

    def excpet2(self, result3):
        """判断保质期很短，请选择保质期"""
        val = ("placeholder")
        num3 = ('xpath', '//*[@class="produce-date flatpickr-input produce-date-error"]')
        num3 = self.b.get_text1(num3, val)
        print num3
        assert num3 == result3

    def excpet3(self, num4):
        """请选择生产日期"""
        val = ("placeholder")
        result3 = ('xpath', '//*[@class="produce-date flatpickr-input"]')
        result3 = self.b.get_text1(result3, val)
        print result3
        assert result3 == num4

    def storage(self, itemcode, itemname, saleprice, vipprice, purprice, purnum, expirydate, standard, marks, result1):
        """自定义商品编码 sheet1"""
        self.input_code(itemcode)
        self.t.time1()
        self.click_name()
        self.input_name(itemname)
        self.t.time1()
        self.click_arrow()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_vip(vipprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.input_standard(standard)
        self.t.time1()
        self.input_marks(marks)
        self.t.time1()
        self.click_storagebutton()
        self.t.time1()
        self.excpet(result1)

    def storage11(self, itemcode, itemname, saleprice, vipprice, purprice, purnum, expirydate, standard, marks, result2):
        """进货价格大于销售价格入库 sheet 销售单价小于进货单价，确定要提交么？"""
        self.input_code(itemcode)
        self.t.time1()
        self.click_name()
        self.input_name(itemname)
        self.t.time1()
        self.click_arrow()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_vip(vipprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.input_standard(standard)
        self.t.time1()
        self.input_marks(marks)
        self.t.time1()
        self.click_storagebutton()
        self.t.time1()
        self.excpet1(result2)

    def storage1(self, itemname, saleprice, vipprice, purprice, purnum, expirydate, standard, marks, result1):
        """点击没有编码测试  sheet2"""
        self.click_NO()
        time.sleep(10)
        self.input_name(itemname)
        self.t.time1()
        self.click_arrow()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_vip(vipprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.input_standard(standard)
        self.t.time1()
        self.input_marks(marks)
        self.t.time1()
        self.click_storagebutton()
        self.t.time1()
        self.excpet(result1)

    def storage17(self, itemname, saleprice, vipprice, purprice, purnum, expirydate, standard, marks, result2):
        """点击没有编码测试  sheet17"""
        self.click_NO()
        time.sleep(10)
        self.input_name(itemname)
        self.t.time1()
        self.click_arrow()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_vip(vipprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.input_standard(standard)
        self.t.time1()
        self.input_marks(marks)
        self.t.time1()
        self.click_storagebutton()
        self.t.time1()
        self.excpet1(result2)

    def storage2(self, expirydate,  num3):
        """保质期验证,判断保质期很短，请选择保质期  sheet3"""
        self.click_NO()
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.click_bad()
        self.t.time1()
        self.excpet2(num3)

    def storage3(self, expirydate,  num4):
        """保质期验证，请选择保质期,验证年份  sheet4"""
        self.click_NO()
        time.sleep(5)
        self.click_expirydate()
        self.t.time1()
        self.click_nian()
        self.t.time1()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.click_bad()
        self.t.time1()
        self.excpet3(num4)

    def storage4(self, expirydate,  num4):
        """保质期验证，请选择保质期,验证月份  sheet5"""
        self.click_NO()
        time.sleep(5)
        self.click_expirydate()
        self.t.time1()
        self.click_month()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.click_bad()
        self.t.time1()
        self.excpet3(num4)

    def storage5(self, expirydate,  num3):
        """保质期验证，保质期很短，请选择保质期,验证月份  sheet6"""
        self.click_NO()
        time.sleep(5)
        self.click_expirydate()
        self.t.time1()
        self.click_month()
        self.input_expirydate(expirydate)
        self.t.time1()
        self.click_bad()
        self.t.time1()
        self.excpet2(num3)

    def storage6(self, itemname, saleprice, purprice, purnum, num2, result1):
        """删除供应商测试   sheet7"""
        self.click_NO()
        self.t.time1()
        self.input_name(itemname)
        self.t.time1()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.click_supplier()
        self.t.time1()
        self.delete_supplier()
        self.t.time1()
        self.excpet1(num2)
        self.t.time1()
        self.click_yes0()
        self.excpet(result1)
        self.click_enter()
        self.t.time1()
        self.click_storagebutton()
        self.t.time1()
        self.click_esc()

    def storage7(self, itemname, saleprice, purprice, purnum, editIpt, result1):
        """修改供应商测试   sheet8"""
        self.click_NO()
        self.t.time1()
        self.input_name(itemname)
        self.t.time1()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.click_supplier()
        self.t.time1()
        self.rename_supplier()
        self.t.time1()
        self.input_supplier(editIpt)
        self.click_enter()
        self.excpet(result1)
        self.t.time1()
        self.click_enter()
        self.click_storagebutton()
        self.t.time1()
        self.click_esc()

    def storage8(self, itemname, saleprice, purprice, purnum, editIpt1, result1):
        """修改商品大类测试   sheet9"""
        self.click_NO()
        self.t.time1()
        self.input_name(itemname)
        self.t.time1()
        self.input_sale(saleprice)
        self.t.time1()
        self.input_pur(purprice)
        self.t.time1()
        self.input_purnum(purnum)
        self.click_sort()
        self.t.time1()
        self.rename_sort()
        self.t.time1()
        self.input_sort(editIpt1)
        self.click_enter()
        self.excpet(result1)
        self.t.time1()
        self.click_enter()
        self.click_storagebutton()
        self.t.time1()
        self.click_esc()

    def storage9(self, result2, result1):
        """删除入库记录 sheet10"""
        self.click_ben()
        self.click_delete()
        self.excpet1(result2)
        self.click_enter()
        self.excpet(result1)
        self.click_enter()

    def storage10(self, result2, result1):
        """删除今日入库记录"""
        self.click_jin()
        self.click_delete()
        self.excpet1(result2)
        self.click_enter()
        self.excpet(result1)
        self.click_enter()


if __name__ == "__main__":
    a = StorageUZG()
    a.open_uzg()
    time.sleep(3)
    a.login_uzg()
    time.sleep(10)
    a.click_storage()
    a.input_shpglframe()
    a.input_shyprkframe()
    time.sleep(3)
    a.storage17("12","12","12","11","12","12","12","12", u"商品采购入库成功是否打印条码，以便贴在柜台或货架上，方便您扫描")