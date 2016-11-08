import cv2
import numpy as np
import math
from autopilot.input import Mouse

#mouse = Mouse.create()
palm = cv2.CascadeClassifier('palm.xml')
fist = cv2.CascadeClassifier('fist.xml')

cap = cv2.VideoCapture(0)

mouseX = 0
mouseY = 0

while(cap.isOpened()):
    ret, img = cap.read()
#    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    handsPalm = palm.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in handsPalm:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	print "palm    ",x+(w/2),"    ",y+(h/2)

    handsFist = fist.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in handsFist:
	mouseX = x + (w/2)
	mouseY = y + (h/2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        print "fist    ",x+(w/2),"    ",y+(h/2)

#    mouse.move(mouseX, mouseY)

    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

