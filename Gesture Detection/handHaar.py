import cv,cv2
import numpy as np
import math
#from autopilot.input import Mouse
from pymouse import PyMouse
#import gtk
 
#width = gtk.gdk.screen_width()
#height = gtk.gdk.screen_height()


m = PyMouse()
#mouse = Mouse.create()
palm = cv2.CascadeClassifier('palm.xml')
fist = cv2.CascadeClassifier('fist.xml')

cap = cv2.VideoCapture(0)
#if (cap.isOpened()==0):
#    print("No Camera")

cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 1000)
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
        mouseX = x + (w/2)
        mouseY = y + (h/2)
	m.click(1000-mouseX,mouseY)
    handsFist = fist.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in handsFist:
	mouseX = x + (w/2)
	mouseY = y + (h/2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        print "fist    ",x+(w/2),"    ",y+(h/2)
#	mouseX = int(mouseX * 2560 / 1000)
#	mouseY = int(mouseY * 2560 / 1000)
#	m.move(2560-mouseX,mouseY)
	m.move(1000-mouseX,mouseY)
#    mouse.move(mouseX, mouseY)
    img = cv2.flip(img,1)
    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

