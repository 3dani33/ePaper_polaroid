"""Script for ..."""
import cv2
import RPi.GPIO as GPIO
from datetime import datetime

import capture
import button
import display

BUTTON_PIN = 4

# setup
print('Starting ePaper polaroid.')
# button
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# display
display.setup()

# main loop
try:
    while True:
        print('Wait for button press...')
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING) # waits until button is pressed
        # generate timestamp for filename
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'{timestamp}.webcam.jpg'
        # capture image and save to file
        image = capture.get_image()
        cv2.imwrite(filename, image)
        # write to display
        display.display_image(filename)
        print('Picture taken and shown!')
except KeyboardInterrupt:
    print('Exiting...')