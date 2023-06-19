import numpy as np

def find_A_matrix(camera_points, world_points):
    """function to find the A matrix

    Args:
        camera_points : Camera Coordinates
        world_points : World Coordinates

    Returns:
         'A' Matrix
    """
    A = []
    for i in range(len(camera_points)):
        u,v = camera_points[i]
        x,y,z = world_points[i]
        A.append([0, 0, 0, 0, -x, -y, -z, -1, v*x, v*y, v*z, v])
        A.append([x, y, z, 1, 0, 0, 0, 0, -u*x, -u*y, -u*z, -u]) 
    return np.asarray(A)

def find_P_matrix(A):
    """function to find the projection matrix

    Args:
        A : 

    Returns:
         Projection matrix
    """
    U, S, Vt = np.linalg.svd(A)
    P = Vt[-1,:] / Vt[-1,-1]
    Px = np.reshape(P,(3,4))
    return Px

def find_K_R_matrix(P):
    """function to find the intrinsic matrix,rotation matrix using Gram Schmidt process

    Args:
        P : Projection Matrix 

    Returns:
        K : Intrinsic Matrix
        R : Rotation Matrix   
    """
    M = []
    M.append(P[:,0])
    M.append(P[:,1])
    M.append(P[:,2])
    M = np.asarray(M).T
    K = np.zeros((3,3))
    R = np.zeros((3,3))
    for i in range(3):
        R[i,i] = np.linalg.norm(M[:,i])
        K[:,i] = M[:,i] / R[i,i]
        for j in range(i+1, 3):
            R[i,j] = np.dot(K[:,i], M[:,j])
            M[:,j] = M[:,j] - R[i,j] * K[:,i]
    return K, R

def find_T_matrix(P):
    """function to get the Translation vector

    Args:
        P : Projection Matrix

    Returns:
        Translation vector
    """
    return np.resize(P[:,3].T,(3,1))

def find_reprojection(camera_points, world_points, P):
    """function to compute the reprojection error

    Args:
        camera_points : camera points 
        world_points : world points
        P  : projection matrix 

    Returns:
        reprojection error
    """
    camera_points_homogeneous = np.column_stack((camera_points, np.ones(len(camera_points))))
    world_points_homogeneous = np.column_stack((world_points, np.ones(len(world_points))))
    projected_camera_points = P @ world_points_homogeneous.T
    projected_camera_points = projected_camera_points / projected_camera_points[2, :]
    error = np.linalg.norm(camera_points_homogeneous.T - projected_camera_points, axis=0)
    return error


camera_points = [(757,213),(758,415),(758,686),(759,966),(1190,172),(329,1041),(1204,850),(340,159)]

world_points = [(0,0,0),(0,3,0),(0,7,0),(0,11,0),(7,1,0),(0,11,7),(7,9,0),(0,1,7)]

A = find_A_matrix(camera_points, world_points)

print("A Matrix:")
print(A)

Px = find_P_matrix(A)
print("\nProjection Matrix P:")
print(Px)

# Get Intrinsic Matrix and Rotation Matrix
K, R = find_K_R_matrix(Px)
print("\nIntrinsic  Matrix K: ")
print(K)
print("\nRotation Matrix R: ")
print(R)

# Get Translation Vector
T = find_T_matrix(Px)
print("\nTranslation Vector T:")
print(T)

# Compute reprojection error
reprojection_error = find_reprojection(camera_points, world_points, Px)
print('Reprojection Error of each point in the image plane')
print('---------------------------------------------------')
for i in range(len(camera_points)):
    print(f" Point ({camera_points[i]}) : {reprojection_error[i]}")
