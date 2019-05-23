# coding=utf-8
import ReadExcel

ab = {}

def param():
    #ab = [[1], [3, 4]]
    return ab

def setParam(pab):
    ab = pab


if __name__ == "__main__":
    a = param()
    filepath = "D:\\Unit_Test\\data\\loginTest.xlsx"
    sheetName1 = "Sheet1"
    sheetName2 = "Sheet2"
    datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data(a[0])
    datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data(a[1])
    # print param()
    # print type(a[0])
    # print a[1]
    # print str(datadict1).decode("unicode_escape").encode("utf8")
    # print str(datadict2).decode("unicode_escape").encode("utf8")