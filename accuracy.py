import os
from PIL import Image
import numpy as np
from pathlib import Path

avgMap = np.zeros(shape=(256,256))
LOC = "data/"
TRUTH =  "DAPI/"
OUT = "test/out/"
counter = 0

for i in range(2024):
    truImg = np.array(Image.open(os.path.join(LOC, TRUTH, "%d.png"%i)))
    outImg = np.array(Image.open(os.path.join(LOC, OUT, "%d_predict.png"%i)))
    for x in range(256):
        for y in range(256):
            diff = abs(truImg[x][y] - outImg[x][y]) ** 2
            avgMap[x][y] = diff

avgMap = (avgMap * 255).astype(np.uint16)
Image.fromarray(avgMap, mode='L;16').save('aggregate.png')


