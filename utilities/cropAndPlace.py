"""
This script will take png images of the size 1024x2048 and crop 1:1 and slightly overlapping crops, so 
it can fit in a publisher file to be printed for a full picture dual page display
"""
import cv2
import shutil
import os

MY_PATH = "."
SPLIT_SIGN = "."
FILE_TYPE = ".png"
CALCULATED_OVERLAP = 1031  # better use a factor for possibly scaled images
NO_OVERLAP = 1024
OVERLAP_VARIANTS = [CALCULATED_OVERLAP, NO_OVERLAP]
CROP_PREFIX = "cr_"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))]

print(onlyfiles)

for i, fileName in enumerate(onlyfiles):
    if fileName.endswith(FILE_TYPE):
        dirName = str(i) + fileName.split(SPLIT_SIGN)[0]
        try:
            os.mkdir(dirName)
        except FileExistsError as e:
            break

        shutil.copy(fileName, dirName)

        im = cv2.imread(fileName)
        imgheight=im.shape[0]
        imgwidth=im.shape[1]
        print(imgheight, imgwidth)
        
        for overlap in OVERLAP_VARIANTS:

            crop1 = im[0:imgheight, 0:overlap].copy()   #[y:y+h, x:x+w]
            crop2 = im[0:imgheight, imgwidth-overlap:imgwidth].copy()  
            cropsList = [crop1, crop2]

            for i, croppedImg in enumerate(cropsList):
                name = CROP_PREFIX + str(overlap)[2:] + "_" + str(i) + fileName
                cv2.imwrite(name, croppedImg)
                shutil.move(name, dirName)


        # cr1FileName = CROP_PREFIX_1 + fileName
        # cr2FileName = CROP_PREFIX_2 + fileName

        # cv2.imwrite(cr1FileName, crop1)
        # cv2.imwrite(cr2FileName, crop2)
        # # move file
        # shutil.move(cr1FileName, dirName)
        # shutil.move(cr2FileName, dirName)



# for all files:
    # make dir with file name
    # copy file into dir

    # crop versions I left, right
        # copy, crop, move
        # copy, crop, move

    # crop version II left, right
        # copy, crop, move
        # copy, crop, move



# file_src = 'source.txt'  
# f_src = open(file_src, 'rb')

# file_dest = 'destination.txt'  
# f_dest = open(file_dest, 'wb')

# shutil.copyfileobj(f_src, f_dest)  