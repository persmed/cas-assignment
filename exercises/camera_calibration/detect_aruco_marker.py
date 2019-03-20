import os
import numpy as np
import cv2
from cv2 import aruco

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 1920, 1080)

# load the calibration parameters
cv_file = cv2.FileStorage("calibration.yaml", cv2.FILE_STORAGE_READ)
mtx = cv_file.getNode("camera_matrix").mat()
dist = cv_file.getNode("dist_coeff").mat()
cv_file.release()

aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while cap.isOpened():
    ret, frame = cap.read()
    #frame = cv2.undistort(frame, mtx, dist, None, None)
    # frame = cv2.undistort(frame, mtx, dist)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
    parameters = aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    font = cv2.FONT_HERSHEY_SIMPLEX  # font for displaying text (below)

    if np.all(ids != None):
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[0], 20, mtx, dist)

        aruco.drawAxis(frame, mtx, dist, rvec[0], tvec[0], 0.025)
        aruco.drawDetectedMarkers(frame, corners)
        pose_r, _ = cv2.Rodrigues(rvec)
        pose = np.eye(4)
        pose[0:3, 0:3] = pose_r
        pose[0:3, 3] = tvec[0]
        print(pose)

        ###### DRAW ID #####
        cv2.putText(frame, "Id: " + str(ids), (0, 64), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the resulting frame
    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
