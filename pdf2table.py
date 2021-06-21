# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:17:36 2021

@author: L380
"""

import pdfplumber
import pandas as pd
#import xlrd
import xlwt

def pdf2Table(pdfpath,excelPath):
    pdf = pdfplumber.open(pdfpath)
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    for page in pdf.pages:
        table = page.extract_tables()
        numT = len(table)
        for k in range(numT):
            # 创建一个worksheet
            worksheet = workbook.add_sheet(f'Sheet{k}')
            # 得到的table是嵌套list类型，转化成DataFrame更加方便查看和分析
            t= table[k]
            df = pd.DataFrame(t[1:], columns=t[0])
            print(df)
            for i in range(len(t)):
                lst = t[i]
                for j in range(len(lst)):
                    worksheet.write(i,j,lst[j])        
    workbook.save(excelPath)

if __name__ == '__main__':
    # 获取文件的路径
    pdfpath ="./00 统计.pdf"
    excelPath = './xlsOut.xls'
    pdf2Table(pdfpath,excelPath)