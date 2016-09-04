import cv2
cap=None

def capture(device=0):
    global cap
    if cap is None:
        cap = cv2.VideoCapture(device)
        print "aki"
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            raise StopIteration("Fim")

        else:

            yield cap.read()


def imshow(img,name="Teste"):
    cv2.imshow(name , img)

