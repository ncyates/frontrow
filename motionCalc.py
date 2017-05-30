#Using a multithreaded approach
#  Necessary Packages
import time
import copy
import cv2
import imutils
from imutils.video import FileVideoStream
from skimage.measure import compare_ssim as ssim

count = 0
s = 0

def compare_frames(frm1, frm2):
    global count
    global s
    s += ssim(frm1, frm2)
    count += 1

def main(vid):
    fvs = FileVideoStream(vid).start()
    time.sleep(.01)
    firstFrame = fvs.read()
    firstFrame = imutils.resize(firstFrame, width=500)
    firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    firstFrame = cv2.GaussianBlur(firstFrame, (21, 21), 0)

    while fvs.more():
        frame = fvs.read()
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        compare_frames(firstFrame, gray)
        firstFrame = copy.deepcopy(gray)
        fvs.read() #uncomment to skip a frame each round

    fvs.stop()
    global s
    s = s / count
    return s, vid

