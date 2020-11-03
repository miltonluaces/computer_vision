import sys
sys.path.append('D:/source/repos')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utilities.std_imports import *
import cv2
from PIL import Image
import pytesseract
import io
from pdf2image import convert_from_path
import os

# image to text
#___________________________________________________________________________________________________________________________________________________________________


def img2txt(img_file, ocr_file):
    img = cv2.imread(img_file)
    txt = pytesseract.image_to_string(img)
    lines = txt.split('\n')
    lines_txt = '\n'.join(lines) + '\n'

    ocr_txt = open(ocr_file,"w") 
    ocr_txt.write(lines_txt) 
    ocr_txt.close()
    print(ocr_file, ' generated.')

def pdf2png(path, txt_name):
    pdf_files = [path + 'pdf/'+ file_name for file_name in os.listdir(path + 'pdf/')]
    for i in range(len(pdf_files)): 
        img = convert_from_path(pdf_files[i])
        img[0].save(path + 'png/' + txt_name + str(i+1) + '.png', 'PNG')
        n_files = len(pdf_files)
        return n_files
    
def png2txt(path, n_files, txt_name):
    for i in range(n_files): 
        img = cv2.imread(path + 'png/' + txt_name + str(i+1) + '.png')
        txt = pytesseract.image_to_string(img)
        lines = txt.split('\n')
        lines_txt = '\n'.join(lines) + '\n'

        ocr_txt = open(path + 'txt/' + txt_name + str(i+1) + '.txt',"w") 
        ocr_txt.write(lines_txt) 
        ocr_txt.close()
        print(txt_name + str(i+1) + '.txt' + ' generated.')
        
        

# TESTING
#____________________________________________________________________________________________________________________________________________________________________

if __name__ == '__main__':
    print('\n')

    