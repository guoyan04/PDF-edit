# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:09:02 2021

@author: L380
"""

import datetime
import os
import fitz  # fitz就是pip install PyMuPDF
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
     PDFInfoNotInstalledError,
     PDFPageCountError,
     PDFSyntaxError
)
import tempfile

class Pdf2ImageApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('PDF文件转换为图片')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.canvas1 = tk.Canvas(self, width=300, height=300, bg='lightsteelblue2', relief='raised')
        self.canvas1.pack()

        # 创建一个容器
        self.panel_method= tk.Frame(self, bg='lightsteelblue2')
        self.label1 = tk.Label(self.panel_method, text='选择转换方法：', bg='lightsteelblue2')
        self.label1.config(font=('宋体', 12, 'bold'))
        self.label1.pack(side='left')
        methods = [
            ("Pdf2Image", 1),
            ("pyMuPDF", 2)]
        self.method = tk.IntVar()
        self.method.set(1)
        for txt, num in methods:
            b = tk.Radiobutton(self.panel_method, text=txt, variable=self.method, value=num, bg='lightsteelblue2')
            b.pack(anchor="w")
        self.canvas1.create_window(150, 50, window=self.panel_method)

        # 创建一个容器
        self.panel_dpi= tk.Frame(self, bg='lightsteelblue2')
        # 创建标签对象和文本框对象并添加到输出文件容器
        self.label_dpi = tk.Label(self.panel_dpi, text='分辨率dpi:', font=('宋体', 12, 'bold'), bg='lightsteelblue2')
        self.label_dpi.pack(side='left')
        addr_dpi = tk.StringVar(value='144')
        self.entry_dpi = tk.Entry(self.panel_dpi, textvariable=addr_dpi)
        self.entry_dpi.pack(side='right')
        #self.panel_dpi.pack()
        self.canvas1.create_window(150, 110, window=self.panel_dpi)

        self.browseButton = tk.Button(self, text="     Select File     ", command=self.getFile, bg='green', fg='white',
                                      font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(150, 150, window=self.browseButton)

        self.saveAsButton = tk.Button(self, text='Convert to IMAGES', command=self.convertToImage, bg='green',
                                      fg='white', font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(150, 190, window=self.saveAsButton)

        self.exitButton = tk.Button(self, text='Exit Application', command=self.exitApplication, bg='brown', fg='white',
                                    font=('helvetica', 12, 'bold'))
        self.canvas1.create_window(150, 230, window=self.exitButton)

    def getFile(self):
        self.import_file_path = filedialog.askopenfilename(
            filetypes=[("PDF", ".pdf")])

    def convertToImage(self):
        self.export_directory = filedialog.askdirectory()
        dpi = int(self.entry_dpi.get())
        if self.method.get() == 1:
            self.pyPdf2Image(self.import_file_path, self.export_directory, dpi)
        if self.method.get() == 2:
            self.pyMuPDF_fitz(self.import_file_path, self.export_directory, dpi)

    def exitApplication(self):
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            self.master.destroy()

    @staticmethod
    def pyPdf2Image(pdfPath, imagePath, dpi):
        #with tempfile.TemporaryDirectory() as path:
            #images_from_path = convert_from_path(pdfPath, output_folder=path, dpi=150)
            # Do something here
        print('using pyPdf2Image')
        images_from_path = convert_from_path(pdfPath, dpi=dpi, fmt='png')
        imagNameList = []
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        for i, image in enumerate(images_from_path):
            image.save(imagePath + '/' + 'usingP2I_%s.png' % i, 'PNG')
            imagNameList.append('usingP2I_%s.png' % i)
        return imagNameList

    @staticmethod
    def pyMuPDF_fitz(pdfPath, imagePath, dpi):
        #startTime_pdf2img = datetime.datetime.now()  # 开始时间

        #print("imagePath=" + imagePath)
        print('using pyMuPDF')
        pdfDoc = fitz.open(pdfPath)
        filename = os.path.basename(pdfPath)
        filenameroot = os.path.splitext(filename)[0]
        imagNameList = []
        for pg in range(pdfDoc.pageCount):
            page = pdfDoc[pg]
            rotate = int(0)
            # 此处若是不做设置，默认图片大小为：dpi=72
            zoom_x = dpi/72.0  # (2-->dpi=144)
            zoom_y = dpi/72.0
            mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pix = page.getPixmap(matrix=mat, alpha=False)

            if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
                os.makedirs(imagePath)  # 若图片文件夹不存在就创建

            pix.writePNG(imagePath + '/' + filenameroot + '_images_%s.png' % pg)  # 将图片写入指定的文件夹内
            imagNameList.append(filenameroot + 'images_%s.png' % pg)
        #endTime_pdf2img = datetime.datetime.now()  # 结束时间
        #print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)
        return imagNameList



if __name__ == "__main__":
    root = tk.Tk()
    app = Pdf2ImageApp(master=root)
    app.mainloop()

"""
    # 1、PDF地址
    pdfPath = 'sample3.pdf'
    # 2、需要储存图片的目录
    imagePath = './imag'
    pyMuPDF_fitz(pdfPath, imagePath)
"""