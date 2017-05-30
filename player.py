import time
import cv2
import sys
import imutils
import numpy as np



if len(sys.argv) > 1:
    print(sys.argv[1])
    camera = cv2.VideoCapture(sys.argv[1])
    time.sleep(0.25)



    while True:
        grabbed, frame = camera.read()
        #frame = imutils.resize(frame)
        #frame = cv2.resize(frame,None,fx = 1, fy = 1)

        cv2.imshow('',frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
