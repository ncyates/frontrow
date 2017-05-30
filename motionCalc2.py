#Using a non-multithreaded approach
# Necessary Packages
from skimage.measure import compare_ssim as ssim
import imutils
import time
import numpy as np
import cv2
import copy

count = 0
s = 0
def compare_frames(frm1, frm2):
    global count
    global s
    s += ssim(frm1, frm2)
    count += 1


def main(vid):
    camera = cv2.VideoCapture(vid)
    grabbed1, firstFrame = camera.read()
    firstFrame = imutils.resize(firstFrame, width=500)
    firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    firstFrame = cv2.GaussianBlur(firstFrame, (21, 21), 0)

    # loop over the frames of the video
    while True:
        (grabbed2, frame) = camera.read()
        if not grabbed2:
            break
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        compare_frames(firstFrame, gray)
        firstFrame = copy.deepcopy(gray)
        camera.read() #uncomment to skip a frame each round

    global s
    s = s / count
    #print(s, vid)
    # print(s, args["video"], "%s seconds" % (time.time() - start_time))

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
    return s, vid
