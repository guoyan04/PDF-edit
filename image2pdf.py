# -*- coding: utf-8 -*-
"""

"""

from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


root = tk.Tk()
root.title('图片转换为PDF')

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getFile():
    global imags
    imags = []
    import_file_paths = filedialog.askopenfilenames(filetypes=[("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")])
    for import_file_path in import_file_paths:
        image1 = Image.open(import_file_path)
        im1 = image1.convert('RGB')
        imags.append(im1)


browseButton = tk.Button(text="     Select File     ", command=getFile, bg='green', fg='white',
                         font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)


def convertToPdf():
    global imags

    export_file_path = filedialog.asksaveasfilename(filetypes=[("PDF", ".pdf")], defaultextension='.pdf')
    im1 = imags[0]
    imagelist = imags[1:]
    im1.save(export_file_path, save_all=True, append_images=imagelist)


saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white',
                         font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='Exit Application', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()