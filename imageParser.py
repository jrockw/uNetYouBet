import numpy as np
import cv2

img = cv2.imread('cancer.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgH = img.shape[0]
imgW = img.shape[1]

y1 = 0
M = imgH//20
N = imgW//20
z=1
for x in range(0,imgW,N):
    for y in range (0, imgH,M):
        y1 = y+M
        x1 = x+N
        tiles = img[y:y+M,x:x+N]

        cv2.rectangle(img, (x,y), (x1, y1), (0,255,0))
        cv2.imwrite("save/"+ str(z) +".png",tiles)
        z = z+1
cv2.imwrite("asas.png", img)
