import os
import random as rd
import shutil
from PIL import Image
def copytree(src, dst, symlinks=False, ignore=None): 
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s): 
            shutil.copytree(s,d,symlinks,ignore)
        else: 
            shutil.copy2(s,d)

def copyWhole(src, dst): 
    img = Image.open(src)
    if (img.size == 256, 256):
        shutil.copy2(src, dst)
    else: 
        print("Image not copied, size: "+ img.size)
        print("File name " + src)
#Missing D2 and B1, these will be reserved for further testing
folders = {"A1", "A2", "A3", "A4", "A5", "A6", "A7", "B2", "B3", "B4", "B5", "B6", "B7", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "D1", "D3", "D4", "D5", "D6", "D7", "E1", "E2", "E3", "E4", "E5", "E6", "E7"}
datashare = "/Datashare/Users/jrockw"
DAPIDest = "/home/jrockw/uNetYouBet/data/train/label"
HEDest = "/home/jrockw/uNetYouBet/data/train/image"
DAPITest = "/home/jrockw/uNetYouBet/data/test/label"
HETest = "/home/jrockw/uNetYouBet/data/test/image"
HEVal = "/home/jrockw/uNetYouBet/data/validation/image"
DAPIVal = "/home/jrockw/uNetYouBet/data/validation/label"
for core in folders: 
    he = os.path.join(datashare, "he", core, "gray")
    DAPI = os.path.join(datashare, "DAPI", core, "inverted")
    HEFiles = os.listdir(he)
    # 10% of dataset per folder
    randomFiles = rd.sample(HEFiles, 355)
    for i in range(202): 
        ind = len(randomFiles[i]) - 4
        num = randomFiles[i][11:ind]
        if (num != "4900"):
            HEFile = os.path.join(he, randomFiles[i])
            DAPIFile = os.path.join(DAPI,"DAPI_" + core + "_invrt-"+num+".png")
            copyWhole(HEFile, HEDest)
            copyWhole(DAPIFile, DAPIDest)
    for i in range(203,304): 
        ind = len(randomFiles[i]) - 4
        num = randomFiles[i][11:ind]
        if (num != "4900"):
            HEFile = os.path.join(he, randomFiles[i])
            DAPIFile = os.path.join(DAPI, "DAPI_" + core + "_invrt-"+num+".png")
            copyWhole(HEFile, HEDest)
            copyWhole(DAPIFile, DAPIDest)
    for i in range(305, 355): 
        ind = len(randomFiles[i]) - 4
        num = randomFiles[i][11:ind]
        if (num != "4900"):
            HEFile = os.path.join(he, randomFiles[i])
            DAPIFile = os.path.join(DAPI, "DAPI_" + core + "_invrt-"+num+".png")
            copyWhole(HEFile, HEDest)
            copyWhole(DAPIFile, DAPIDest)
        
        
    #TRAIN AND TEST, GET RID OF WHITE? 

