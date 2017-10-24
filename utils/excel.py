# -*- coding: utf-8 -*-

import xlrd

class Excel(object):
    def __init__(self, file):
        self.__file = file

    def open_excel(self):
        try:
            data = xlrd.open_workbook(self.__file)
            return data
        except Exception, ex:
            print(str(ex))

    def get_data_by_name(self, name=u'Sheet1', row_start=0, col_start=0, row_end=0, col_end=0):
        data = self.open_excel()
        table = data.sheet_by_name(name)
        nrows = table.nrows
        ncols = table.ncols

        if row_start < 0 or row_start > nrows:
            row_start = 0
        if col_start < 0 or col_start > ncols:
            col_start = 0
        if row_end < 0 or row_end > nrows:
            row_end = nrows
        if col_end < 0 or col_end > ncols:
            col_end = ncols

        data_list = [[] for i in range(0, row_end - row_start)]

        for rowNum in range(row_start, row_end):
            rowContent = table.row_values(rowNum)
            for colNum in range(col_start, col_end + 1):
                cellContent = rowContent[colNum]
                data_list[rowNum - row_start].append(cellContent)
        return data_list

if __name__ == '__main__':
    excel = Excel('D:\\Downloads\\thinkpage_cities\\ChinaCities.xls')
    data_list = excel.get_data_by_name(name=u'中国地级市', row_start=1, col_start=1, row_end=1, col_end=1)
    print(data_list)














