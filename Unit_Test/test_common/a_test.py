# coding=utf-8


def AB():
    ab = [[1, 2], [3, 4]]
    return ab

if __name__ == "__main__":
    import ReadExcel
    a = AB()
    filepath = "D:\\Unit_Test\\data\\loginTest.xlsx"
    sheetName1 = "Sheet1"
    sheetName2 = "Sheet2"
    datadict1 = ReadExcel.ExcelUtil(filepath, sheetName1).dict_data(a[0])
    datadict2 = ReadExcel.ExcelUtil(filepath, sheetName2).dict_data(a[1])
    print AB()
    print AB()[0]
    print AB()[1]
    print datadict1
    print datadict2
    # print a[0]
    # print a[1]