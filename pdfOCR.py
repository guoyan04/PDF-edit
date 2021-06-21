# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:13:17 2021

@author: L380
"""
import os
import pdf2imag
import baiduOCR

def pdfOCR(pdfPath,txtdir):
    if not os.path.exists(txtdir):  # 判断文件夹是否存在
            os.makedirs(txtdir)  # 若文件夹不存在就创建
    imagedir = txtdir +'/imag_tmp'
    imagNameList = pdf2imag.Pdf2ImageApp.pyPdf2Image(pdfPath, imagedir, 200)
    text = ''
    for ImName in imagNameList:
        text += baiduOCR.img_to_str(imagedir+'/'+ImName)
    return text

if __name__ == '__main__':
    
    pdfPath = '党风廉政建设讲话.pdf'
    txtdir = './pdfOCR'
    text = pdfOCR(pdfPath,txtdir)
    fs = open(txtdir+'/pdfOCR.txt', 'w+')  # 将str,保存到txt
    fs.write(text)
    fs.close()
    print("识别完成。")