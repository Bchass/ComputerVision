from cv2 import cv2
import numpy as np

# Line 8: Calculates frames, width & height
# Line 9: How frames are getting compressed
# Line 10: Takes compressed frames and does magic with the frames
# Line 11: Init blob detector
vid = cv2.VideoCapture(r'/Users/bchass/Documents/git/3DMapping/videos/new.mp4')
size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(r'E:/6.avi', fourcc, 30, size)
params = cv2.SimpleBlobDetector_Params()

# Check fps and resolution
if vid.isOpened():

     FPS = vid.get(cv2.CAP_PROP_FPS)
     print ('FPS: ', FPS)
     print('Resolution: ',size)


while(1):
    ret, frame = vid.read()
    if not ret:
        break
    
    frame = cv2.convertScaleAbs(frame)
    params = cv2.SimpleBlobDetector_Params()
 
    # thresholds
    params.minThreshold = 100
    params.maxThreshold = 112

    # Area
    params.filterByArea = True
    params.minArea = 60

    # Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1

    # Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87

    # Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Blob detector picks up params
    ver = (cv2.__version__).split('.')

    if int(ver[0]) < 3 :
	    detector = cv2.SimpleBlobDetector(params)
    else : 
	    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    with_kp = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # If video is open calls keypoints to be displayed
    if ret == True:
        video.write(with_kp)
        cv2.imshow('frame', with_kp)
    else:
        vid.release()
        break
    # Close out / pause video
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1)
