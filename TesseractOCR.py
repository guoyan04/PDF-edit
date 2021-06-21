# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:23:38 2021

@author: L380
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'
imag = Image.open('./imag/001.jpg')
text = pytesseract.image_to_string(imag,lang='chi_sim')

print(text)