import numpy as np
import cv2

board_w = 11
board_h = 8

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 1920, 1080)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w * board_h, 3), np.float32)
objp[:, :2] = np.mgrid[0:board_w, 0:board_h].T.reshape(-1, 2)
objp *= 15
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
img_shape = None
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
save_next = False

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_shape = gray.shape
    # Find the chess board corners
    ret, corners = cv2.findCirclesGrid(gray, (board_w, board_h), None)  #
    cv2.drawChessboardCorners(frame, (board_w, board_h), corners, ret)
    # If found, add object points, image points (after refining them)
    if ret and save_next:
        objpoints.append(objp)
        imgpoints.append(corners)
        print(len(objpoints))
        save_next = False

    cv2.imshow("Image", frame)
    key = cv2.waitKey(5)
    if key == ord('n'):
        break
    if key == ord(' '):
        save_next = True
    if key == ord('q'):
        exit()

calib_flags = cv2.CALIB_SAME_FOCAL_LENGTH + cv2.CALIB_FIX_K4 + cv2.CALIB_FIX_K5 + cv2.CALIB_FIX_K6
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_shape, None, None, flags=calib_flags)
h, w = img_shape[:2]

print('error: ', ret)
print('camera matrix: ', mtx)
print('distortion: ', dist)

cv_file = cv2.FileStorage("calibration.yaml", cv2.FILE_STORAGE_WRITE)
cv_file.write("camera_matrix", mtx)
cv_file.write("dist_coeff", dist)
cv_file.release()
axis = np.float32([[20, 0, 0], [0, 20, 0], [0, 0, -20]]).reshape(-1, 3)


# Function to draw the axis
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
    return img


while cap.isOpened():
    ret, frame = cap.read()
    # undistort
    dst = cv2.undistort(frame, mtx, dist)
    cv2.imshow("Undistored", dst)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findCirclesGrid(gray, (board_w, board_h), None)
    if ret:
        _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)
        # project 3D points to image plane
        imgpts, _ = cv2.projectPoints(objp, rvecs, tvecs, mtx, dist)
        axispts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        frame = draw(frame, corners, axispts)

        for pts in imgpts:
            if pts[0, 0] > 1000 or pts[0, 0] < 0 or pts[0, 1] > 1000 or pts[0, 1] < 0:
                continue
            frame = cv2.circle(frame, (pts[0, 0], pts[0, 1]), 4, (255, 0, 0), -1)
        for corner in corners:
            frame = cv2.circle(frame, (corner[0, 0], corner[0, 1]), 1, (0, 255, 0), -1)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
print("done")
