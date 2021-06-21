# -*- coding: utf-8 -*-
"""
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def PdfSplit(infn,splitPath):
    pdf_input = PdfFileReader(open(infn, 'rb'))
    # 获取 pdf 共用多少页
    page_count = pdf_input.getNumPages()
    if not os.path.exists(splitPath):  # 判断存放拆分文件的文件夹是否存在
        os.makedirs(splitPath)  # 若拆分文件夹不存在就创建
    for i in range(page_count):
        pdf_output = PdfFileWriter()
        pdf_output.addPage(pdf_input.getPage(i))
        #outfns=f'{splitPath}/split-{i+1}.pdf'
        pg=i+1
        outfns = splitPath + '/' + 'split_%s.pdf' % pg
        pdf_output.write(open(outfns, 'wb'))

if __name__ == '__main__':
    infn = 'sample1.pdf'
    splitPath = './splitout'
    PdfSplit(infn, splitPath)