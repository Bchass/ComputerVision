import cv2
import numpy as np

vid = cv2.VideoCapture('')
# open video, display pixels, RGB, etc..
while(vid.isOpened()):
    ret,frame = vid.read()
    cv2.imshow('frame',frame)
# kill the video
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()