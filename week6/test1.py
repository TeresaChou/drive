import numpy as np
import cv2 

cap = cv2.imread("ya.jpg")



    
#ret, frame = cap.read()												# Capture frame-by-frame
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)						# Our operations on the frame come here


orb = cv2.ORB_create()												# Initiate ORB detector
kp = orb.detect(gray,None)											# find the keypoints with ORB	
kp, des = orb.compute(gray, kp)										# compute the descriptors with ORB
img2 = cv2.drawKeypoints(gray, kp, None, color=(0,255,0), flags=0)	# draw only keypoints location,not size and orientation

'''
fast = cv2.FastFeatureDetector_create(threshold=25)					# Initiate FAST detector
kp = fast.detect(gray,None)											# Find and draw the keypoints
img2 = cv2.drawKeypoints(gray, kp, None,color=(255,0,0))			# draw only keypoints location,not size and orientation
'''

cv2.imwrite('frame.jpg',img2)											# Display the resulting framek

