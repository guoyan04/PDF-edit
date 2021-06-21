# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:58:19 2021

@author: L380
对本地保存的pdf文件进行读取和写入到txt文件当中

"""
#import sys
#import importlib
#importlib.reload(sys)

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextBoxHorizontal, LTTextLine
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed

# 定义解析函数
def pdftotxt_pdfminer(path,new_name):
    # 创建一个文档分析器
    parser = PDFParser(open(path,'rb'))
    # 创建一个PDF文档对象存储文档结构
    document =PDFDocument(parser)
    # 连接分析器 与文档对象
    #parser.set_document(document)
    #document.set_parser(parser)
    
    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    #document.initialize()
    # 判断文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储资源
        resmag =PDFResourceManager()
        # 设定参数进行分析
        laparams =LAParams()
        # 创建一个PDF设备对象
        #device=PDFDevice(resmag)
        device =PDFPageAggregator(resmag,laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(resmag, device)
        # 处理每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout =device.get_result()
            for y in layout:
                if(isinstance(y,LTTextBoxHorizontal)):
                    with open("%s"%(new_name),'a',encoding="utf-8") as f:
                        f.write(y.get_text())

if __name__ == '__main__':
    # 获取文件的路径
    path ="./sample4.pdf"
    pdftotxt_pdfminer(path,"./pdfminer.txt")
