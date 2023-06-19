# Camera Calibration and Image Processing in Autonomous Robots
This project is part of the ENPM673 - Perception for Autonomous Robots coursework. The focus is on camera calibration using Python, NumPy, and OpenCV.

## Dependencies
- Python 3.7+
- NumPy
- OpenCV

## Instructions to Run the Code
Ensure you have the required dependencies installed in your environment. Python scripts and sample images are provided in the repository.

1. Clone this repository using the command: `git clone https://github.com/kiranajith/Camera-calibration-.git`
2. Navigate to the directory: `cd YourRepositoryName`
3. Run the Python scripts using the command: `python script_name.py`

Ensure you include the correct relative path of the images and calibration text file.

## Problem 1
In Problem 1, we manually calibrate the camera by computing the intrinsic matrix, P matrix, and then decomposing the P matrix into the Translation, Rotation, and Intrinsic matrices using the Gram–Schmidt process. Reprojection error for each point is also calculated. 

Python script for this problem: 
- problem1.py

## Problem 2
In Problem 2, we perform camera calibration using in-built functions of OpenCV, starting with corner detection on a checkerboard image. The calibration is carried out for a series of images taken from different angles and positions to optimise the computed camera matrix, known as the K matrix. The reprojection error for each image is also computed. 

Python scripts for this problem:
- problem2.py

A detailed explanation for the steps involved is given in the report


## Acknowledgments
This project is a part of ENPM673 - Perception for Autonomous Robots at the University of Maryland, College Park.

