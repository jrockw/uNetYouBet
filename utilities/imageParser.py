import numpy as np
import cv2
from PIL import Image

Image.MAX_IMAGE_PIXELS = 999999999 
img = cv2.imread('/Datashare/Segmentation/he_s00/20190116_TMA-2-HE__01/TMA-2-HE__01_B-1.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destoryAllWindows()
imgH = img.shape[0]
imgW = img.shape[1]

y1 = 0
M = imgH//20
N = imgW//20
z=0
for x in range(0,imgW,N):
    for y in range (0, imgH,M):
        y1 = y+M
        x1 = x+N
        tiles = img[y:y+M,x:x+N]

        cv2.rectangle(img, (x,y), (x1, y1), (0,255,0))
        cv2.imwrite("data/he/"+ str(z) +".png",tiles)
        z = z+1
