"""
452 project1
Author:
Haiyu Zhang
Kai Yan
Shikan Lian
last date:11/06/2019
"""
"""
this program creates a marker library contains 250 random markers of 5*5 size
Press 's' to save a result in the folder:./image/marker
press 'esc' to break out
"""

import cv2.aruco as aruco
import cv2
import numpy as np

number = 13
# create a dictionary includes 250 marker, each marker sizes 5*5bits
dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
img = np.random.random((200, 200))

# create the marker image, use the 23rd marker in the dictionary, 200*200 pixels, boundary size=1
img = aruco.drawMarker(dict, number, 200, img, 1)

while 1:
    cv2.imshow('marker', img)  # show the marker
    k = cv2.waitKey(10)
    if k == 27:  # esc 27
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):  # press s key to save marker
        cv2.imwrite('./image/marker/marker.jpg', img)
        print('marker saved')
