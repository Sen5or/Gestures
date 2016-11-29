import subprocess
import time
import cv2
import sys

subprocess.call("python face_recognize.py",shell=True)
subprocess.call("pkill -f face_recognize.py",shell=True)
#a = time.time()
while(1):
    subprocess.call("python handTracking.py ",shell=True)
    key = cv2.waitKey(10)
    if key == 27:
	break
sys.exit()


