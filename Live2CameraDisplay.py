import numpy as np
import cv2

h=800
v=600

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

#Set up cameras
cap0.set(3,h)
cap0.set(4,v)
cap0.set(10,0.5)

cap1.set(3,h)
cap1.set(4,v)
cap1.set(10,0.5)

while(True):
    ret,frame0 = cap0.read()
    ret,frame1 = cap1.read()

    cv2.imshow('frame0',frame0)
    cv2.imshow('frame1',frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
	break
cap0.release()
cap1.release()
