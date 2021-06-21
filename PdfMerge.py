# -*- coding: utf-8 -*-
"""
"""

from PyPDF2 import PdfFileMerger
def PdfMerge(pdfs, output):
    # 创建一个pdf文件合并对象
    Merger = PdfFileMerger()
    # 逐个添加pdf
    for pdf in pdfs:
        f = open(pdf, 'rb')
        Merger.append(f)
    # 将内存中合并的pdf文件写入
    fout= open(output, 'wb')
    Merger.write(fout)


if __name__ == '__main__':
    # 需要合并的pdf名称
    pdfs = ['sample1.pdf', 'sample2.pdf']
    # 合并完成的pdf名称
    output = 'combined_example.pdf'
    # 调用PDFmerge函数，进行合并
    PdfMerge(pdfs, output)