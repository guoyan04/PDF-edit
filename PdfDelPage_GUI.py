# -*- coding: utf-8 -*-
"""
PDF文件删除页
"""
import tkinter
import tkinter.messagebox
from PdfDelPage import PdfDelPage

def delPDFpage_GUI():
    # 删除页
    def deletePDfpage():
        infn = entry_input.get()
        outfn = entry_output.get()
        s = entry_pageNum.get()
        deletePages = [int(i) for i in s.split(',')]
        PdfDelPage(infn, outfn, deletePages)
    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            wd.destroy()

    # 创建窗口
    wd = tkinter.Tk()
    # 设置窗口大小
    wd.geometry('300x150')
    # 设置窗口标题
    wd.title('删除PDF页')

    # 创建一个装输入文件名的容器
    panel_input = tkinter.Frame(wd)
    # 创建标签对象和文本框对象并添加到输入文件容器
    label_input = tkinter.Label(panel_input, text='输入文件：', font=('宋体', 12), fg='black')
    label_input.pack(side='left')
    addr_input = tkinter.StringVar(value='./sample1.pdf')
    entry_input = tkinter.Entry(panel_input, textvariable=addr_input)
    entry_input.pack(side='right')
    panel_input.pack(side='top')

    # 创建一个装输出文件名的容器
    panel_output = tkinter.Frame(wd)
    # 创建标签对象和文本框对象并添加到输出文件容器
    label_output = tkinter.Label(panel_output, text='输出文件：', font=('宋体', 12), fg='black')
    label_output.grid(row=0, column=0)
    addr_output = tkinter.StringVar(value='./deleteOut.pdf')
    #addr_output = tkinter.StringVar()
    entry_output = tkinter.Entry(panel_output, textvariable=addr_output)
    #entry_output.insert(0, './deleteOut.pdf')
    entry_output.grid(row=0, column=1)
    panel_output.pack()

    # 创建一个装输入删除页码的容器
    panel_pageNum = tkinter.Frame(wd)
    # 创建标签对象和文本框对象并添加到输出文件容器
    label_pageNum = tkinter.Label(panel_pageNum, text='删除页码：', font=('宋体', 12), fg='black')
    label_pageNum.pack(side='left')
    addr_pageNum = tkinter.StringVar(value='2,3,4')
    entry_pageNum = tkinter.Entry(panel_pageNum, textvariable=addr_pageNum)
    entry_pageNum.pack(side='right')
    panel_pageNum.pack()

    # 创建一个装按钮的容器
    panel = tkinter.Frame(wd)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='删除页', font=('宋体', 12), command=deletePDfpage)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', font=('宋体', 12), command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack()
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    delPDFpage_GUI()