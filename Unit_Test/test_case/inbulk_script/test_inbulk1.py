# coding=utf-8

import unittest
import ddt
from test_common import ReadExcel
from test_common import Storage_inbulk
import os

filepath = "D:\\Unit_Test\\data\\inbulkTest.xlsx"
# filepath = os.getcwd() + ("\\data\\inbulkTest.xlsx")
sheetName1 = ("Sheet1")
sheetName2 = ("Sheet2")
sheetName3 = ("Sheet3")
sheetName4 = ("Sheet4")
sheetName5 = ("Sheet5")
sheetName6 = ("Sheet6")
datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data()
datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data()
datadict3 = ReadExcel.ExcelUtil(filepath, sheetName3).dict_data()
datadict4 = ReadExcel.ExcelUtil(filepath, sheetName4).dict_data()
datadict5 = ReadExcel.ExcelUtil(filepath, sheetName5).dict_data()
datadict6 = ReadExcel.ExcelUtil(filepath, sheetName6).dict_data()


@ddt.ddt
class InbulkTest(unittest.TestCase,):
    """新建散货测试"""
    a = Storage_inbulk.StorageUZG()

    @classmethod
    def setUpClass(cls):
        cls.a.open_uzg()
        cls.a.login_uzg()
        cls.a.click_storage()
        cls.a.storage_iframe()
        cls.a.stroage_inbulk()
        cls.a.click_inbulk()
        cls.a.click_newstorage()

    @classmethod
    def tearDownClass(cls):
        cls.a.storage_free()
        cls.a.storage_free()
        cls.a.quit_uzg()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*datadict1)
    def test_inbulk01(self, dat1):
        """新建散货—商品名称输入测试"""
        print dat1
        self.a.storage1(dat1['itemname'], dat1[u'result'])

    @ddt.data(*datadict2)
    def test_inbulk02(self, dat2):
        """新建散货—销售价格输入测试"""
        print dat2
        self.a.storage2(dat2['itemname'], dat2['saleprice'], dat2[u'result'])

    @ddt.data(*datadict3)
    def test_inbulk03(self, dat3):
        """新建散货—进货价格输入测试"""
        print dat3
        self.a.storage3(dat3['itemname'], dat3['saleprice'], dat3['purprice'], dat3['purnum'], dat3[u'result'])

    @ddt.data(*datadict4)
    def test_inbulk04(self, dat4):
        """新建散货—商品单位测试"""
        print dat4
        self.a.storage4(dat4['itemname'], dat4['saleprice'], dat4[u'result'])

    @ddt.data(*datadict5)
    def test_inbulk05(self, dat5):
        """新建散货—新建成功提示测试"""
        print dat5
        self.a.storage5(dat5['itemname'], dat5['saleprice'], dat5['vipprice'], dat5['purprice'], dat5['purnum'], dat5['standard'], dat5[u'result'])

    @ddt.data(*datadict6)
    def test_inbulk06(self, dat6):
        """新建散货—成功后—在入库记录验证测试"""
        print dat6
        self.a.storage6(dat6[u'result'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)