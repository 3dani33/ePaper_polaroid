"""Capture an image from the webcam with openCV."""
import cv2

def get_image():
    cam = cv2.VideoCapture(0)
    # read image multiple times to allow camera to adjust exposure
    for i in range(10):
        _, frame = cam.read()
    return frame

if __name__ == '__main__':
    cv2.imwrite('temp.jpg', get_image())
