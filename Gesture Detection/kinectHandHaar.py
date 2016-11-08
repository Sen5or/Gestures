#import the necessary modules
import freenect
import cv2
import numpy as np
import math

palm = cv2.CascadeClassifier('palm.xml')
fist = cv2.CascadeClassifier('fist.xml')

 
#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    while 1:
        #get a frame from RGB camera
        frame = get_video()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        handsPalm = palm.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in handsPalm:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            print "palm    ",x+(w/2),"    ",y+(h/2)

        handsFist = fist.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in handsFist:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            print "fist    ",x+(w/2),"    ",y+(h/2)

        cv2.imshow('img',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
