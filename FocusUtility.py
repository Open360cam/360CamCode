import numpy as np
import cv2

#Utility for setting lens focus
#Creates zoome view of each camera near the center of the image circle
#Hit q to close

#Set preview resolution
h=800
v=600

#Set cam 0
cap0 = cv2.VideoCapture(0)
cap0.set(3,h)
cap0.set(4,v)
cap0.set(10,0.5)

#Test for Cam0
ret,frame0 = cap0.read()

if ret == 'False':
   print 'Cam0 not found'

print 'Cam0 found'

#Set cam 1
cap1 = cv2.VideoCapture(1)
cap1.set(3,h)
cap1.set(4,v)
cap1.set(10,0.5)

#Test for Cam1
ret,frame0 = cap0.read()
if ret == 'False':
   print 'Cam1 not found'
   
print 'Cam1 found'

while(ret):
    ret,frame0 = cap0.read()
#    cv2.imshow('Full frame0', frame0)    #show full frame for reference
   
    frame0Crop = frame0[220:400, 400:600]  
    r = 400/frame0Crop.shape[1]
    dim = (400, int(frame0Crop.shape[0] * r))
    frame0Crop = cv2.resize(frame0Crop,dim , interpolation = cv2.INTER_AREA) 

    ret,frame1 = cap1.read()
#    cv2.imshow('Full frame1', frame1)    #show full frame for reference
    frame1Crop = frame1[200:400, 350:500]  

    r = 400/frame1Crop.shape[1]
    dim = (400, int(frame1Crop.shape[0] * r))
    frame1Crop = cv2.resize(frame1Crop,dim , interpolation = cv2.INTER_AREA) 


#    cv2.imshow('frame0',frame0)
#    cv2.imshow('frame1',frame1)
	
    cv2.imshow('frame0',frame0Crop)
    cv2.imshow('frame1',frame1Crop)

    if cv2.waitKey(1) & 0xFF == ord('q'):
	cap0.release()
	cap1.release()
	break

