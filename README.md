# ePaper Polaroid
Instant pictures with a Raspberry Pi, a webcam and a ePaper display:

![Demonstration](img/demo.gif)

![](img/img_webcam.bmp)

![](img/img_cropped.bmp)

![](img/img_resized.bmp)

![](img/img_binary.bmp)

# Components
## Install openCV

https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-install-opencv-raspberry-pi/

Get an image from the webcam: capture.py

## Button
use builtin RPi.GPIO library and a simple pushbutton
bcm mode, because of display driver

## Display
https://www.waveshare.com/wiki/1.54inch_e-Paper_Module

## load image and convert to black and white
using Pillow (PIL fork)

