import numpy as np
import cv2

#Set preview resolution
h=800
v=600

#Set cam 0
cap0 = cv2.VideoCapture(0)
cap0.set(3,h)
cap0.set(4,v)
cap0.set(10,0.5)

#Set cam 1
cap1 = cv2.VideoCapture(1)
cap1.set(3,h)
cap1.set(4,v)
cap1.set(10,0.5)

while(True):
    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()

    cv2.imshow('frame0',frame0)
    cv2.imshow('frame1',frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
	cap0.set(14,0)  # gain
	cap0.set(3,2592)
	cap0.set(4,1944)
	cap0.set(10,0.001)
	# 3 frames to make sure setting are updated
	ret,fullframe0 = cap0.read()
	ret,fullframe0 = cap0.read()  
	ret,fullframe0 = cap0.read()
 	cv2.imwrite('Cam0_2592x1944frame.jpg',fullframe0)
	cap0.release()

	cap1.set(14,0)  # gain
	cap1.set(3,2592)
	cap1.set(4,1944)
	cap1.set(10,0.001)
	# 3 frames to make sure setting are updated
	ret,fullframe1 = cap1.read()
	ret,fullframe1 = cap1.read()  
	ret,fullframe1 = cap1.read() 
 	cv2.imwrite('Cam1_2592x1944frame.jpg',fullframe1)
	cap1.release()

	break

