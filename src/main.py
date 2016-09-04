from capture.video import capture,imshow
from segmentation.pontosDeInteresse import findEyes,findFace
from threading import Thread


def run():

    for i in capture(0):
        qtdFace, img = findFace(i[1], True)
        #qtdOlhos,img=findEyes(i[1])

        if qtdFace==0:
            print "Nao detectado"
        imshow(img)
if __name__=="__main__":

    r = Thread(run())
    r.join()


