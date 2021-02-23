from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2

# Inicia stream de video
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop frames
while True:
    # Lê um frame
    frame = vs.read()
    # Define tamanho máximo para 400 pixels
    frame = imutils.resize(frame, width=400)

    # rotina para detectar face e pontos ...

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # verifica se pressinou f
    if key == ord("f"):
        cam = cv2.VideoCapture(0)
        ret_val, img = cam.read()

        cv2.imshow("Camera", img) #if you wanted to open a window to see this picture
        cv2.waitKey(0)
        break

    # verifica se pressinou x
    if key == ord("x"):
	    break

# Limpeza do ambiente
cv2.destroyAllWindows()
vs.stop()
