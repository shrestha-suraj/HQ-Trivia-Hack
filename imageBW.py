from PIL import Image
import numpy as np

#This function converts a colorful image to black and white so that
# # pytesseract can have ease to recognize the texts.
#  
image1=Image.open("sample.jpg")
image1=np.float32(image1)
for x in range (0,len(image1)):
    for y in range (0,len(image1[x])):
        if not((image1[x][y]==[0.0,0.0,0.0]).all()):
            image1[x][y]=[255.0,255.0,255.0]
image1.save("sampleBW.jpg")