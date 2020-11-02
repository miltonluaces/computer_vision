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


# image to text
#___________________________________________________________________________________________________________________________________________________________________


def img2txt(img_file, ocr_file):
    img = cv2.imread(img_file)
    txt = pytesseract.image_to_string(img)
    lines = txt.split('\n')
    lines_txt = '\n'.join(lines) + '\n'

    ocr_txt = open("ocr.txt","w") 
    ocr_txt.write(lines_txt) 
    ocr_txt.close()
    print(ocr_file, ' generated.')
    

# TESTING
#____________________________________________________________________________________________________________________________________________________________________

if __name__ == '__main__':
    print('\n')

    