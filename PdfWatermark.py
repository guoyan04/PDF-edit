# -*- coding: utf-8 -*-
"""
有待完善
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from copy import copy

def PdfWatermark(infn, outfn, wmfn):
    wm_page = PdfFileReader(wmfn).getPage(0)
    output = PdfFileWriter()
    input = PdfFileReader(open(infn, "rb"))
    page_count = input.getNumPages()
    for i in range(page_count):
        page = input.getPage(i)
        #page.mergePage(wm_page)
        new_page = copy(wm_page)
        new_page.mergePage(page)
        output.addPage(new_page)
    output.write(open(outfn,'wb'))

if __name__ == '__main__':
    infn = 'sample1.pdf'
    outfn = 'WmOut.pdf'
    wmfn = 'watermark.pdf'
    PdfWatermark(infn, outfn, wmfn)