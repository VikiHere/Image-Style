'''
Hard Thresholding
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
from PIL import Image

def main(*arg):
    print("Format: python average_images.py *list of image names*")
    imgName = input("Please enter image name: ")
    t = input("Please enter the threshold: ")
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint32')

    out = hard_threshold(img, (float)(t)).astype('uint8')      
    final = Image.fromarray(out)
    final.show()
    final.save("hard_threshold_test.png")


def hard_threshold(img, T):
    out_img = img

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k = img[i][j]/255
            if (k < T):
                out_img[i][j] = (int)(0)
            else:
                out_img[i][j] = (int)(255)
    
    #print(out_img)
    return out_img

if __name__ == '__main__':
    main()