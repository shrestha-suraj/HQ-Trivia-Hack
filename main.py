#install pytesseract using command pip intall Pillow and pip install pytesseract
import pytesseract
from PIL import Image
import argparse
import cv2
import os

ap=argparse.ArgumentParser()
ap.add_argument("i","./",required=True)
ap.add_argument("-p","thresh",type=str,default="thresh")
args=vars(ap.parse_args())
image=cv2.imread("sample.jpg",0)
gray=cv2.cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#image=Image.open("sample.jpg")
#print(pytesseract.image_to_string(image))