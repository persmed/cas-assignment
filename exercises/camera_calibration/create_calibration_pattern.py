import os
import numpy as np
import cv2
from cv2 import aruco

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

board = aruco.CharucoBoard_create(8, 6, 1, 0.8, aruco_dict)
imboard = board.draw((8000, 6000))
imboard_show = cv2.resize(imboard, (800, 600))

cv2.imshow("Charuco", imboard_show)
cv2.waitKey(0)
chessboard_file = os.path.join('data', 'charuco_board.png')
cv2.imwrite(chessboard_file, imboard)
