#coding=utf-8
import xlrd


class ExcelUtil(object):
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # print str(self.keys).decode("unicode_escape").encode("utf8")
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []  # 把此注释掉
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    ctype = self.table.cell(j, x).ctype
                    if ctype == 2:
                        s[self.keys[x]] = int(values[x])
                    else:
                        s[self.keys[x]] = values[x]
                r.append(s)  # 把此注释掉
                j += 1
            return r  # 把此改为s，则最后格式为字典格式，用于接口自动化的传参

if __name__ == "__main__":
    filepath = "C:\\Users\\wanghengli\\Desktop\\111.xlsx"
    sheetName = "Sheet1"
    dictdata = ExcelUtil(filepath, sheetName)
    datadict1 = ExcelUtil(filepath, sheetName).dict_data()
    print str(datadict1).decode("unicode_escape").encode("utf8")






    # filepath = "D:\\Unit_Test\\data\\loginTest.xlsx"
    # sheetName = "Sheet1"
    # dictdata = ExcelUtil(filepath, sheetName)
    # datadict1 = ExcelUtil(filepath, sheetName).dict_data()
    # print str(datadict1).decode("unicode_escape").encode("utf8")
    # print "--------------------"





    # print str(datadict1[0:4]).decode("unicode_escape").encode("utf8")
    # def num(num1, ber1):
    #     data = ExcelUtil(filepath, sheetName).dict_data()[num1:ber1]
    #     print data
    # num(0, 1)

    # print(dictdata.cell(1, 2).value)
    # print(dictdata.cell_value(1, 2))
    # print(dictdata.row(1)[2]).value
    # print(dictdata.col(2)[1]).value

    # print str(data.dict_data()).decode("unicode_escape").encode("utf8")
    # for i in dictdata.dict_data():
    #     print str(i).decode("unicode_escape").encode("utf8")

    # a = dictdata.dict_data()
    # rows = a.row_values(1)
    # cols = a.col_values(0)
    # print("rows:%s \n cols:%s" % (rows, cols))