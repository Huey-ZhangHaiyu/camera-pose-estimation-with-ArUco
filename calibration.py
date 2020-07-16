"""
452 project1
Author:
Haiyu Zhang
Kai Yan
Shikan Lian
last date:11/06/2019
"""
"""
This program uses the calibration image in the folder:./image/calibration 
to calculate the camera ’s matrix and distortion coefficients matrix
"""

import cv2
import numpy as np
import glob


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)  # threshold
# chessboard size
w = 9  # 10 - 1 number of corner
h = 6  # 7  - 1

# chess block in global frame, cancel the z axis
objp = np.zeros((w * h, 3), np.float32)
objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)
# each block sizes 19 mm
objp = objp * 19

# save corner of chess block's 3D and 2D coordinates
objpoints = []  # 3D points in global frame
imgpoints = []  # 2D points in image frame

# read the image from folder:./image/Calibration
images = glob.glob('./image/Calibration/*.jpg')

i = 1
for fname in images:
    img = cv2.imread(fname)  # read the image one at a time
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB image to gray image
    # find the corner
    ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
    # save the corner
    if ret:  # if find the corner
        print("i:", i)
        i = i + 1

        # use the cornerSubPix() to get a more accurate coordinates
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners)

        # show the corner
        cv2.drawChessboardCorners(img, (w, h), corners, ret)
        cv2.namedWindow('findCorners', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('findCorners', 810, 405)
        cv2.imshow('findCorners', img)
        cv2.waitKey(1)
cv2.destroyAllWindows()

# calibration
ret, mtx, dist, rvecs, tvecs = \
    cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("ret:", ret)
print("mtx:\n", mtx)  # camera matrix
print("dist:\n", dist)  # distortion coefficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs:\n", rvecs)  # rotation
print("tvecs:\n", tvecs)  # translation
