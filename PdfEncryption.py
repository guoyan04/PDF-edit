# -*- coding: utf-8 -*-
"""
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

def PdfEncryption(infn, outfn, password):
    output = PdfFileWriter()
    input = PdfFileReader(open(infn, "rb"))

    page_count = input.getNumPages()
    for i in range(page_count):
        page = input.getPage(i)
        output.addPage(page)

    #output.cloneDocumentFromReader(input)  #改方法存在错误

    output.encrypt(password)
    output.write(open(outfn,'wb'))

if __name__ == '__main__':
    infn = 'sample3.pdf'
    outfn = 'EncryptionOut.pdf'
    password = 'abcdefg'
    PdfEncryption(infn, outfn, password)