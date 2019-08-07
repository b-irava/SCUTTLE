import cv2
import numpy as np
import L1_camera as cam

def colorTracking(img, color_range=((0,0,0),(255,255,255))):

    global image

<<<<<<< HEAD
    image = img

    if filter == 'RGB':
        frame_to_thresh = image.copy()
    else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert image to hsv colorspace RENAME THIS TO IMAGE_HSV

    # thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max)) # Converts a 240x160x3 matrix to a 240x160x1 matrix
    thresh = cv2.inRange(frame_to_thresh, (color_range[0][0], color_range[0][1], color_range[0][2]), (color_range[1][0], color_range[1][1], color_range[1][2])) # Converts a 240x160x3 matrix to a 240x160x1 matrix
    # cv2.inrange discovers the pixels that fall within the specified range and assigns 1's to these pixels and 0's to the others.

    # apply a blur function
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) # Apply blur
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # Blur again

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2] #generates number of contiguous "1" pixels
    center = None # create a variable for x, y location of target

    if len(cnts) > 0:   # begin processing if there are "1" pixels discovered

        c = max(cnts, key=cv2.contourArea)  # return the largest target area
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        # # M = cv2.moments(c)
        # # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))  # defines a circle around the largest target area
        # center = (int(x), int(y))  # defines a circle around the largest target area

        return ((round(x,1),round(y,1)),round(radius,1))

    else:

        return((None, None), 0)

####################################################

color_range = ((0,180,130),(10,255,255))

# width  = 240  # please attempt to put back into the function
# height = 160

while True:

    # image = cam.takepic((width,height))
    image = cam.takepic()

    # image = cv2.resize(image,(width,height)) # resize the image

    ((x, y), radius) = colorTracking(image, color_range)

    print(x,y, "\t", radius)
=======
        return ((x,y),radius)

    def build_image(self, img):

        return all

def init_filter():
    f = MyFilter()
    return f.process

while 1:
    color_range = ((0,180,130),(10,255,255))
>>>>>>> 6172cd6ddd4eff90e903bcb2c470fa0b5a061f43
