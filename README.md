#Face Recognition and Gesture Recognition
Run python mainCode.py

Dependencies:
Subprocess, cv, cv2, time, sys, freenect, subprocess, numpy, os, Xlib

# Gestures Recognition

I have developed 2 different methods for Hand Gesture recognition:

#Method 1:

##Installation instruction:

1.libfreenect for Kinect

https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/

2.Pygame:

sudo apt-get install python-pygame

3.Numpy:

sudo apt-get install python-numpy

4.Opencv:

sudo apt-get install python-opencv

5.Xlib for mouse control:

sudo apt-get install python-Xlib

##Test instructions:

1.python handTracking.py

2.Move hand within certain distance threshold to move mouse, palm gesture move mouse and fist gesture clicks the mouse.

3.Click ctrl+c to close program


#Method 2:

This method usses HaarCascade Classifiers

##Installation instruction: 

Code is tested on Ubuntu Laptop

1.libfreenect for Kinect

https://naman5.wordpress.com/2014/06/24/experimenting-with-kinect-using-opencv-python-and-open-kinect-libfreenect/

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev

git clone git://github.com/OpenKinect/libfreenect.git

cd libfreenect

mkdir build

cd build

cmake -L ..

make

sudo make install

sudo ldconfig /usr/local/lib64/

sudo nano /etc/udev/rules.d/51-kinect.rules

--> add following lines:

<nowiki /># ATTR{product}=="Xbox NUI Motor"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02b0", MODE="0666"

<nowiki /># ATTR{product}=="Xbox NUI Audio"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ad", MODE="0666"

<nowiki /># ATTR{product}=="Xbox NUI Camera"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ae", MODE="0666"

<nowiki /># ATTR{product}=="Xbox NUI Motor"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02c2", MODE="0666"

<nowiki /># ATTR{product}=="Xbox NUI Motor"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02be", MODE="0666"

<nowiki /># ATTR{product}=="Xbox NUI Motor"

SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02bf", MODE="0666"

--> Save file and test below line:

freenect-glview

--> In order to use kinect with opencv run below commands:

sudo apt-get install cython

sudo apt-get install python-dev

sudo apt-get install python-numpy

--> Navigate to /libfreenect/wrappers/python and run following command:

sudo python setup.py install

-->Now you can try python kinectHandHaar.py after connecting Kinect:


2.Install opencv

sudo apt-get install python-opencv

3.Library for mouse control:

sudo pip install PyUserInput

--> Now you are all set for Gesture control

#Author

##Dhanesh Girish Pradhan
