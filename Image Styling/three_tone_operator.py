'''
 three tone operator
Vic S.

 NOTE: Scipy and Numpy are only used for matrix manipulations and
        image import
'''

import numpy as np
import sys
import math
from PIL import Image

def main(*arg):
    print("Format: python average_images.py *list of image names*")
    imgName = input("Please enter image name: ")
    #t = input("Please enter the threshold: ")
    u = input("Please enter the sharp transition controller: ")
    img = np.asarray(Image.open(imgName).convert('L'), dtype='uint32')

    out = three_tone(img, (float)(u)).astype('uint8')      
    final = Image.fromarray(out)
    final.show()
    final.save("three_tone_test.png")


def three_tone(img, u):
    out_img = img

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k = img[i][j]/255
        #First tone, the darker intensities
            if (k < 0.33):# 1st ~1/3rd of 255
                #T from the original equation becomes the Max value for this section
                out_img[i][j] = (int)( ( 1 + math.tanh( (int)(u*(k - 0.33)) ) )*out_img[i][j] )
        #Second tine, the middle range intensities
            elif (k >= 0.33 and k < 0.66):# 2nd ~1/3rd of 255
                #T from the original equation becomes the Max value for this section
                out_img[i][j] = (int)( ( 1 + math.tanh( (int)(u*(k - 0.66)) ) )*out_img[i][j] )
        #third tone, the brighter intensities
            else:# 3rd ~1/3rd of 255
                out_img[i][j] = (int)(255)

    #print(out_img)
    return out_img

if __name__ == '__main__':
    main()