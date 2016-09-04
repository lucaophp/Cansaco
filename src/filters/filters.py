import cv2 as cv
from scipy.ndimage import filters
from skimage import data, img_as_float
import numpy as np

def bgr2gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# slow
def rgb2bgr(img):
    nimg = img.copy()
    nimg[::, ::, 0] = img[::, ::, 2]
    nimg[::, ::, 2] = img[::, ::, 0]
    return nimg
def mediana(img,size=3):
    # type: (ndimage, integer) -> ndimage
    return filters.median_filter(img,size=size)
def media(img,size=3):
    mascara=np.ones((3, 3),np.int)
    print mascara
    return filters.correlate(img,mascara,mode='constant', cval=0)
