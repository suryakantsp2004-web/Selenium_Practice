from xlrd import *


def read_locators(path,sheet_name):

    workbook = open_workbook(path)
    sheet = workbook.sheet_by_name(sheet_name)
    count = sheet.nrows
    d = {}
    for i in range(1,count):
        data = sheet.row_values(i)
        d[data[0]] = [data[1],data[2]]
    return d


def read_data(path,sheet_name):
    workbook = open_workbook(path)
    sheet = workbook.sheet_by_name(sheet_name)
    count = sheet.nrows
    l = []
    for i in range(1,count):
        data = sheet.row_values(i)
        l.append(data)
    return l




