"""
452 project1
Author:
Haiyu Zhang
last date:11/06/2019
"""
"""
This program uses the camera ’s matrix and distortion coefficients matrix 
to calculate the rotation vector and the translation vector of the marker in camera frame
Press 's' to save a result in: rvec.txt and tvec.txt
press 'esc' to break out
"""

import numpy as np
import time
import cv2
import cv2.aruco as aruco

mtx = np.array([  # camera matrix
    [930.08031951, 0, 626.59736866],
    [0, 928.83930935, 382.82622809],
    [0.00, 0.00, 1]])
# distortion coefficients matrix
dist = np.array([0.108351177, 0.0641898016, 0.00502687721, -0.000468861045, -0.937800931])

font = cv2.FONT_HERSHEY_PLAIN  # font for displaying text below

# a frame without rotation and translation, use this to verify the camera matrix and distortion coefficients matrix
# if this frame displays in the middle of the picture, the matrix is right
t0 = np.array([0.00, 0.00, 0.00])


def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]) + '\n')
    print(filename, 'saved')
    file.close()


# read the image
img = cv2.imread('./5.jpg')
frame = img
while True:
    # operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()

    # lists of ids and the corners belonging to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        print('id is', ids)  # print out the detected ids
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.048, mtx, dist)
        # Estimate pose of each marker(sizes 0.048m) and return the rotation vector and translation vector
        (rvec - tvec).any()  # get rid of that nasty numpy value array error

        # Draw an axis and a square around the markers
        for i in range(rvec.shape[0]):
            aruco.drawAxis(frame, mtx, dist, rvec[i, :, :], tvec[i, :, :], 0.03)
            aruco.drawDetectedMarkers(frame, corners)

            # draw ID
            cv2.putText(frame, "Id: " + str(ids), (0, 64), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    aruco.drawAxis(frame, mtx, dist, t0, t0, 0.03)

    # Display the resulting frame
    cv2.imshow("frame", frame)

    key = cv2.waitKey(10)
    if key == 27:  # press esc to exit
        print('esc break...')
        # cap.release()
        cv2.destroyAllWindows()
        break
    if key == ord('s'):  # press s to save image and vector
        filename = str(time.time())[:10] + ".jpg"
        cv2.imwrite(filename, frame)
        text_save(rvec, './rotation.txt')  # save rotation vector in rotation.txt
        text_save(tvec, './translation.txt')  # save translation vector in translation.txt
