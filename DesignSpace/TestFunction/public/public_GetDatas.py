# coding=utf-8
# 获取外部数据
import xlrd,os
from DesignSpace.TestFunction.public.public_debug import *

class get_excelDatas():
    def __init__(self):
        self.AllData = {}
        #path = "/".join([os.getcwd(), "TestSpace", "TestDatas", FileName])
        path = r"E:\自动化\GUIPytest_Demo\TestSpace\TestDatas\TestDatas_1.xls"
        excelBook = xlrd.open_workbook(filename=path)
        table = excelBook.sheet_by_name(excelBook.sheet_names()[0])
        tablerows, tableCols = table.nrows, table.ncols
        for num in range(0,tableCols):
            # print(table.col_values(num))
            value = table.col_values(num)
            self.AllData[value[0]]= value[1:]
        logging.info(f"{self.AllData}")

    def getData(self, *args):
        basePara = len(self.AllData[args[0]]) # 基准参数 行数
        logging.info(f"{basePara}")
        tmpList = []
        for x in range(basePara):
            tmpList.append([])
        for colValue in args:
            '''列循环'''
            for key, value in enumerate(self.AllData[colValue]):
                value = str(int(value)) if isinstance(value,float) else value
                if isinstance(value,str) and '[' in value and ']' in value:
                    value = value[1:-1].split(",")
                    tmpList[key].append([x for x in value if x])
                else:
                    # logging.info(f"else:{value}")
                    tmpList[key].append(value)
        logging.info(f"{tmpList}")
        if len(tmpList[0]) == 1:
            return tmpList[0]
        return tmpList

if __name__ == '__main__':
    gd = get_excelDatas()
    sa = gd.getData("DeviceUrl")
    #sa = get_excelDatas.getData(r"D:\相关文档\自动化\GUIPytest_Demo\TestSpace\TestDatas\TestDatas_1.xls")
    print(sa)