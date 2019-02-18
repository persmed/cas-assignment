import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7*9,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:9].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
img_shape = None
cap = cv2.VideoCapture(0)
save_next = False

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_shape = gray.shape
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,9), None)
    # If found, add object points, image points (after refining them)
    if ret == True and save_next:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(frame, (7,9), corners2, ret)
        print(len(objpoints))
        save_next = False

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
    if key == ord(' '):
        save_next = True

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_shape, None, None)
h,  w = img_shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
print('error: ', ret)
print('camera matrix: ', mtx)
print('distortion: ', dist)

while cap.isOpened():
    ret, frame = cap.read()
    # undistort
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    cv2.imshow("Image", dst)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
