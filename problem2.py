import numpy as np
import cv2
import glob 

CHECKERBOARD_SIZE = (9, 6)
SQUARE_SIZE = 21.5 

points = np.zeros((CHECKERBOARD_SIZE[0] * CHECKERBOARD_SIZE[1], 3), np.float32)
points[:, :2] = np.mgrid[0:CHECKERBOARD_SIZE[0], 0:CHECKERBOARD_SIZE[1]].T.reshape(-1, 2) * SQUARE_SIZE

object_points = []
image_points = []

images = glob.glob('/Users/kiranajith/Downloads/Calibration_Imgs/*.jpg')
i=0
for image in images:
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD_SIZE, None)

    if ret:
        object_points.append(points)
        image_points.append(corners)
        cv2.drawChessboardCorners(img, CHECKERBOARD_SIZE, corners, ret)
        cv2.imwrite(f"/Users/kiranajith/Documents/UMD/673/kiran99_proj3/output/img_{i}_corners.jpg", img)
        i+=1

ret, K, dist, rot_vec, trans_vecs = cv2.calibrateCamera(object_points, image_points, gray.shape[::-1], None, None)

print('K matrix: \n', K)
print("\nReprojection Error For Each image")
print("---------------------------------\n")
mean_error = 0
for i in range(len(object_points)):
    image_points2, _ = cv2.projectPoints(object_points[i], rot_vec[i], trans_vecs[i], K, dist)
    error = cv2.norm(image_points[i], image_points2, cv2.NORM_L2) / len(image_points2)
    mean_error += error
    print(f'Image {i+1}: {error}' )
    
print("Mean reprojection error:", mean_error/len(object_points))