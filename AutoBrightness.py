# code to capture a frame.
# importing the required libraries
import cv2                              # to capture the frame
import numpy as np                      # find brightness of the image
import screen_brightness_control as sbc
import os

# Capturing the surrounding with the webcam and saving it.
camera = cv2.VideoCapture(0)
_, image = camera.read()
cv2.imwrite('opencv0.png',image)

# Measuring the brightness of the captured image.
image = cv2.imread('opencv0.png')
L,A,B = cv2.split(cv2.cvtColor(image,cv2.COLOR_BGR2LAB))
L=L/np.max(L)
bright = np.mean(L)*100

current = sbc.get_brightness()
disp = sbc.list_monitors()

sbc.fade_brightness(bright, start= current)

for i in range(1, len(disp)):
    sbc.set_brightness(bright,display=disp[i])

# Deleting the frame captured at the beginning
os.remove('opencv0.png')