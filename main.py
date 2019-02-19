#install pytesseract using command pip intall Pillow and pip install pytesseract
import pytesseract
from PIL import Image

filename1=input("Enter image file: ")
def img2str(filename):
    image=Image.open(filename)
    string1=pytesseract.image_to_string(image,lang='eng')
    print(string1)
img2str(filename1)
# ap=argparse.ArgumentParser()
# ap.add_argument("i","./",required=True)
# ap.add_argument("-p","thresh",type=str,default="thresh")
# args=vars(ap.parse_args())
# image=cv2.imread("sample.jpg",0)
# gray=cv2.cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# image=Image.open("sample.jpg")
# print(pytesseract.image_to_string(image))