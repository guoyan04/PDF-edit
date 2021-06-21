# -*- coding: utf-8 -*-
"""
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def PdfDelPage(infn, outfn, deletePages):
    output = PdfFileWriter()
    input = PdfFileReader(open(infn, "rb"))
    page_count = input.getNumPages()
    for i in range(page_count):
        if i+1 in deletePages:
            continue
        output.addPage(input.getPage(i))
    output.write(open(outfn,'wb'))

if __name__ == '__main__':
    infn = './sample1.pdf'
    outfn = './deleteOut.pdf'
    deletePages = [2,3,4]
    PdfDelPage(infn, outfn, deletePages)
    