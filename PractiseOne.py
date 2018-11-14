#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import xlwt

# 初始化Excel
workbook = xlwt.Workbook(encoding='utf-8')

# 创建一个sheet
sheet = workbook.add_sheet("库存状态", cell_overwrite_ok=True)

def csvTOXls(f):
    with open(f, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        listReader = list(reader)
        print(listReader)
        listReaderHead = listReader[0]  # excel表头
        # print(listReaderHead)
        listReaderContent = listReader[1:len(listReader)]   # Excel内容
        # print(listReaderContent)
        listReaderContent.sort()
        print(listReaderContent)

        # 设置Excel表头样式，背景色“蓝色”，字体“粗体”
        styleHead = xlwt.XFStyle()  # 初始化样式
        # 设置背景颜色
        pattern = xlwt.Pattern()
        # 设置背景颜色的模式
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 背景颜色
        pattern.pattern_fore_colour = xlwt.Style.colour_map['blue']

        # 设置字体
        font = xlwt.Font()  # 创建字体
        # font.name = u'微软雅黑'  # 字体类型
        font.bold = True  # 粗体

        styleHead.font = font  # 设定样式
        styleHead.pattern = pattern

        # 设置状态为无货的样式 在“类型”上标志背景色“黄色”
        styleOutOfStack = xlwt.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']
        styleOutOfStack.pattern

        # 设置“价格”为“空”的记录，在“类型”上标志背景色“红色”
        styleNullPrice = xlwt.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
        styleNullPrice.pattern

        # 写表头
        firstLine = str(listReaderHead[0]).split('，')
        k = 0
        for var in firstLine:
            sheet.write(0, k, var, styleHead)
            k = k + 1

        # 写内容
        for data in listReaderContent:
            i = 1
            if len(data):
                ContentLine = str(data).split("，")
                for var in ContentLine:
                    j = 0
                    if var == "无货":
                        sheet.write(i, j, var, styleOutOfStack)
                        j = j + 1
                    if len(ContentLine) < 4:
                        sheet.write(i, j, var, styleNullPrice)
                        j = j + 1
                    sheet.write(i, j, var)
                    j = j + 1

            i = i + 1
        workbook.save('k.xls')

if __name__ == '__main__':
    csvTOXls("kucun.csv")