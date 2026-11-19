import cv2
import numpy as np

FILTER = 5


def videoFeed():
    #defines the webcam to be used
    cam = cv2.VideoCapture(0)

    #fail-safe for cam not opening
    if not cam.isOpened():
        print("Error - Camera couldn't be opened")  
        raise 'CameraNotFound'

    while True:
        #pulls frame from cam feed
        ret, frame = cam.read()

        #checks frame was successfully retrieved
        if not ret:
            print("Error - Failed to capture frame")
            break

        #gets offset
        offset = sun_identification(frame)

        #calculates offset and prints 
        if offset is not None:
            print('X offset: ' + str(offset[0]))
            print('Y offset: ' + str(offset[1]))

        #releases resources and terminates program if 'q' pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def sun_identification(src):

    #checks image was loaded correctly
    if src is None: 
        print("Error - File not found")
        raise FileNotFoundError

    #changes image to black and white
    image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #blur to reduce noise and to help prevent false circle detection
    image = cv2.medianBlur(image, FILTER)

    #gets image dimensions 
    h, w = image.shape

    #runs the hough circle algorithm and stores position of the sun
    sun = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, h/16, param1=50, param2=10, minRadius=0, maxRadius=0)

    #calculates centre of the sun
    center = 0

    if sun is None:
        print("SunNotFound")

    if sun is not None:
        sun = np.uint16(np.around(sun))

        #gets center of the sun
        for i in sun[0, :]:
            center = (i[0], i[1])

        #calculates and returns the distance the sun is from the centre
        offsetY = abs(h/2 - center[1])
        offsetX = abs(w/2 - center[0])
        return offsetX, offsetY

if __name__ == '__main__':
    videoFeed()