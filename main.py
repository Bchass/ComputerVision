import cv2
import numpy as np

# Line 8: Calculates frames, width & height
# Line 9: How frames are getting compressed
# Line 10: Takes compressed frames and does magic with the frames
# Line 11: Init blob detector
vid = cv2.VideoCapture(r'/Users/brandonchasser/git/SLAM/videos/road.mp4')
size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(r'E:/6.avi', fourcc, 30, size)
params = cv2.SimpleBlobDetector_Params()


while(1):
    ret, frame = vid.read()
    if not ret:
        break
    frame = cv2.convertScaleAbs(frame)
    params = cv2.SimpleBlobDetector_Params()

    # thresholds
    params.minThreshold = 100;
    params.maxThreshold = 112;

    # Area
    params.filterByArea = 1
    params.minArea = 1

    # Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Convexity
    params.filterByConvexity = True
    params.minConvexity = 1

    # Inertia
    params.filterByInertia = 1
    params.minInertiaRatio = 1

    # Blob detector picks up params
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
	    detector = cv2.SimpleBlobDetector(params)
    else : 
	    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    with_kp = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    if ret == True:
        video.write(with_kp)
        cv2.imshow('frame', with_kp)
    else:
        vid.release()
        break
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break