from PIL import Image
import numpy as np

#This function converts a colorful image to black and white so that
# # pytesseract can have ease to recognize the texts.
#  
def imageChange(imagefile):
    image=Image.open(imagefile)
    image=np.float32(image)
    print(type(image[0][0]))
    each=list(image[0][0])
    print(each)

    # for x in range (0,len(image)):
    #     for y in range (0,len(image[x])):
    #         print (str(image[x][y]))
#            if not(image[x][y]=[0.0,0.0,0.0]):
#                image[x][y]=[255.0,255.0,255.0]
imageChange("sample.jpg")