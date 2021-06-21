# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:48:43 2021

@author: L380
"""

import pdfplumber

def pdftotxt(path,new_name):
    
    pdf = pdfplumber.open(path)
    txt = ''
    for page in pdf.pages:
        # 获取当前页面的全部文本信息，包括表格中的文字
        # print(page.extract_text()) 
        text=page.extract_text()
        if text:
            txt= txt+page.extract_text()+'\n'  
    with open("%s"%(new_name),'a',encoding="utf-8") as f:
        f.write(txt+'\n')

if __name__ == '__main__':
    # 获取文件的路径
    path ="./sample4.pdf"
    pdftotxt(path,"./pdfplumber.txt")

