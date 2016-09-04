import cv2 as cv
from filters.filters import bgr2gray,mediana,media
import numpy as np
from scipy.ndimage import filters

def findEyes(img,crop=False):
    eye = cv.CascadeClassifier('../haarcascades/haarcascade_lefteye_2splits.xml')
    olhos = eye.detectMultiScale(bgr2gray(img), 1.3, 5)
    nimg=np.array(img)
    for (xo, yo, lo, ao) in olhos:
        cv.rectangle(img, (xo, yo), (xo + lo, yo + ao), (255, 0, 0), 2)
        nimg.append(img[xo:xo + lo, yo:yo + ao])
        # img.append(crop_img[yo:yo+altura,xo:xo+largura])
        # gray=cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
        if crop is True:
            return len(olhos), nimg

    return len(olhos), img


def findFace(img,crop=False):
    eye = cv.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
    faces = eye.detectMultiScale(bgr2gray(img), 1.3, 5)
    img=mediana(img,3)
    for (xo, yo, lo, ao) in faces:
        cv.rectangle(img, (xo, yo), (xo + lo, yo + ao), (255, 0, 0), 2)
        # img.append(crop_img[yo:yo+altura,xo:xo+largura])
        # gray=cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
        nimg = img[xo:xo + lo, yo:yo + ao]

        if crop is True:
            olhos=findEyes(nimg,True)
            for i in olhos[1]:
                # Operadores de Sobel
                sob_h = np.array([[-1., -2., -1.],
                                  [0., 0., 0.],
                                  [1., 2., 1.]], dtype=float)
                sob_v = np.array([[-1., 0., 1.],
                                  [-2., 0., 2.],
                                  [-1., 0., 1.]], dtype=float)
                # Gradiente de Sobel.
                im_sob_h = filters.correlate(i, sob_h, mode='constant', cval=0)
                im_sob_v = filters.correlate(i, sob_v, mode='constant', cval=0)
                # Magnitude do gradiente (hipotenusa)
                im_sob = np.sqrt(im_sob_h ** 2 + im_sob_v ** 2)
                cv.imwrite("t.png",im_sob)


            return len(faces),nimg

    return len(faces), img






