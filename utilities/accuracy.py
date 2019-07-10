import os
from PIL import Image
import numpy as np

avgMap = np.zeros(shape=(256,256))
LOC = "~/uNetYouBet/data/"
counter = 0 
for file in os.listdir(LOC):
    print (file)
