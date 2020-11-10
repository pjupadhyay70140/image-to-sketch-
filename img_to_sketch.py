# import this four libraries first numpy, imageio, scipy, opencv-python
# scipy only work with numpy


import numpy as np
import imageio
import scipy.ndimage
import cv2

img="DSCN9765.JPG" # enter your image name or path

def grayscale(rgb): # convert the image to balck and white image
	return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back): # to draw the outlines or to blur the image 
	result=front*255/(255-back)
	result[result>255]=255
	result[back==255]=255
	return result.astype('uint8')



s=imageio.imread(img) # image store in this 
g=grayscale(s) 
i=255-g

b=scipy.ndimage.filters.gaussian_filter(i,sigma=50) # sigma is a blur index.
r=dodge(b,g)

cv2.imwrite('sketch_output2.png',r) # enter the output file name 