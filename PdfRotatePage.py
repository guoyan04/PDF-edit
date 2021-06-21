# -*- coding: utf-8 -*-
"""
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def PdfRotatePage(infn, outfn, pages, degree):
    output = PdfFileWriter()
    input = PdfFileReader(open(infn, "rb"))
    page_count = input.getNumPages()
    for i in range(page_count):
        if i+1 in pages:
            newpage = input.getPage(i).rotateClockwise(degree)
            output.addPage(newpage)
        else:
            output.addPage(input.getPage(i))
    output.write(open(outfn,'wb'))

if __name__ == '__main__':
    infn = 'sample1.pdf'
    outfn = 'RotateOut.pdf'
    pages = [1,2]
    degree = 180  #（0，90,180，270）角度必须是90度的整数倍
    PdfRotatePage(infn, outfn, pages, degree)