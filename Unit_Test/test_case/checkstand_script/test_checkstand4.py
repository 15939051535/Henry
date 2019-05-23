# coding=utf-8

import unittest
import ddt
import time
from test_common import ReadExcel
from test_common import Checkstand_package2


filepath = ("D:\\Unit_Test\\data\\checkstandTest.xlsx")
sheetName14 = ("Sheet14")
sheetName15 = ("Sheet15")
sheetName16 = ("Sheet16")
sheetName17 = ("Sheet17")
sheetName18 = ("Sheet18")
# sheetName8 = ("Sheet8")
datadict14 = ReadExcel.ExcelUtil(filepath, sheetName14).dict_data()
datadict15 = ReadExcel.ExcelUtil(filepath, sheetName15).dict_data()
datadict16 = ReadExcel.ExcelUtil(filepath, sheetName16).dict_data()
datadict17 = ReadExcel.ExcelUtil(filepath, sheetName17).dict_data()
datadict18 = ReadExcel.ExcelUtil(filepath, sheetName18).dict_data()
# datadict8 = ReadExcel.ExcelUtil(filepath, sheetName8).dict_data()


@ddt.ddt
class LoginTest (unittest.TestCase):

    a = Checkstand_package2.right()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        time.sleep(7)
        cls.a.click_shyt()
        cls.a.input_shytiframe()

    @classmethod
    def tearDownClass(cls):
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        self.a.click_huiche()

    @ddt.data(*datadict14)
    def test_login14(self, dat14):
        """选择热卖商品销售"""
        print dat14
        self.a.login14(dat14['vip'], dat14['barCode'],  dat14[u'str1'], dat14[u'str2'], dat14[u'str3'], dat14[u'str4'])

    @ddt.data(*datadict15)
    def test_login15(self, dat15):
        """修改热卖商品销售数量"""
        print dat15
        self.a.login15(dat15['vip'], dat15['barCode'], dat15['unPackedSaleNum'],  dat15[u'str1'], dat15[u'str2'],
                      dat15[u'str3'], dat15[u'str4'])

    @ddt.data(*datadict16)
    def test_login5(self, dat16):
        """修改热卖商品销售金额"""
        print dat16
        self.a.login16(dat16['vip'], dat16['barCode'], dat16['unPackedSaleCount'], dat16[u'str1'],
                      dat16[u'str2'], dat16[u'str3'], dat16[u'str4'])

    @ddt.data(*datadict16)
    def test_login6(self, dat16):
        """修改热卖商品销售金额挂单取单销售"""
        print dat16
        self.a.login17(dat16['vip'], dat16['barCode'], dat16['unPackedSaleCount'], dat16[u'str1'],
                      dat16[u'str2'], dat16[u'str3'], dat16[u'str4'])

    @ddt.data(*datadict17)
    def test_login7(self, dat17):
        """修改热卖商品销售金额挂单取单销售免一元销售"""
        print dat17
        self.a.login18(dat17['vip'], dat17['barCode'], dat17['unPackedSaleCount'], dat17[u'str1'],
                      dat17[u'str2'], dat17[u'str3'], dat17[u'str4'])

    @ddt.data(*datadict18)
    def test_login8(self, dat18):
        """修改热卖商品销售金额挂单取单销售免十元内元加修改实际金额销售"""
        print dat18
        self.a.login19(dat18['vip'], dat18['barCode'], dat18['unPackedSaleCount'], dat18['payM'], dat18[u'str1'],
                      dat18[u'str2'], dat18[u'str3'], dat18[u'str4'])

    # """编辑新散货销售"""
    # @ddt.data(*datadict8)
    # def test_login4(self, dat9):
    #     print dat9
    #     self.a.logini(dat9['vip'], dat9['barCode'], dat9['salePrice'], dat9['saleNum'], dat9['purchasePriceInput'],
    #                   dat9['purchaseNumInput'], dat9['str1'], dat9['str2'], dat9['str3'], dat9['str4'])

if __name__ == "__main__":
    unittest.main(verbosity=2)