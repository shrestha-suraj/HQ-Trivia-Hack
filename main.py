#install pytesseract using command pip intall Pillow and pip install pytesseract
import pytesseract
from PIL import Image

filename1=input("Enter image file: ")
def img2str(filename):
    image=Image.open(filename)
    string1=pytesseract.image_to_string(image,lang='eng')
    print(string1)
    
img2str(filename1)