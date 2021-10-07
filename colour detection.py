import cv2
import numpy as np

def empty(a):
    pass

#img  = cv2.imread('anime1.jpg')
image = cv2.VideoCapture(0)
#img = cv2.resize(imgae , (600,400))
#hueee image
#imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#creting trackbar to see the change in real time
cv2.namedWindow('TRACKBAR')
cv2.resizeWindow('TRACKBAR',600,240)
cv2.createTrackbar('HUE MIN' , 'TRACKBAR', 0 , 179 , empty)
cv2.createTrackbar('HUE MAX' , 'TRACKBAR', 179 , 179 , empty)
cv2.createTrackbar('SAT MIN' , 'TRACKBAR', 0 , 255 , empty)
cv2.createTrackbar('SAT MAX' , 'TRACKBAR', 255 , 255 , empty)
cv2.createTrackbar('VAL MIN' , 'TRACKBAR', 0 , 255 , empty)
cv2.createTrackbar('VAL MAX' , 'TRACKBAR', 255,255 , empty)

while True:

    success, img = image.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #to take the position of trackbar
    h_min = cv2.getTrackbarPos('HUE MIN' , 'TRACKBAR')
    h_max = cv2.getTrackbarPos('HUE MAX' , 'TRACKBAR')
    s_min = cv2.getTrackbarPos('SAT MIN' , 'TRACKBAR')
    s_max = cv2.getTrackbarPos('SAT MAX' , 'TRACKBAR')
    v_min = cv2.getTrackbarPos('VAL MIN' , 'TRACKBAR')
    v_max = cv2.getTrackbarPos('VAL MAX' , 'TRACKBAR')
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([[h_max,s_max,v_max]])
    
    mask = cv2.inRange(imghsv , lower , upper)
    
    imgREsult = cv2.bitwise_and(img,imghsv, mask= mask)
    cv2.imshow('OUTPUT',img)
    cv2.imshow('hue',imghsv)
    cv2.imshow('Result' , imgREsult)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
            break
