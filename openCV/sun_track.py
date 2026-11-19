import cv2
import numpy as np

def pre_processing(src):

    FILTER = 5

    #checks image was loaded correctly
    if src is None: 
        print("Error - File not found")
        raise FileNotFoundError

    #changes image to black and white
    image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #blur to reduce noise and to help prevent false circle detection
    image = cv2.medianBlur(image, FILTER)
    return image

def hough(img):

    #gets image dimensions 
    h, w = img.shape

    #runs the hough circle algorithm and stores position of the sun
    sun = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, h/16, param1=50, param2=10, minRadius=0, maxRadius=0)
    return sun

def offset_calc(img):

    #gets image dimensions 
    h, w = img.shape
    
    #calculates centre of the sun
    center = 0

    if img is None:
        print("SunNotFound")

    if img is not None:
        img = np.uint16(np.around(sun))

        #gets center of the sun
        for i in img[0, :]:
            center = (i[0], i[1])

        #calculates and returns the distance the sun is from the centre
        offsetY = int((h/2 - center[1]))
        offsetX = int((w/2 - center[0]))
        return offsetX, offsetY