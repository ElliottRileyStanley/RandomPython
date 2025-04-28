import numpy as np
import math

def project_block_to_image(x, y, z, image_size=1000, fov_deg=70, yaw_deg=45, pitch_deg=45):
    # Convert degrees to radians
    yaw = math.radians(yaw_deg)
    pitch = math.radians(pitch_deg)
    fov = math.radians(fov_deg)

    # Camera intrinsics
    cx = image_size / 2
    cy = image_size / 2
    f = (image_size / 2) / math.tan(fov / 2)  # focal length in pixels

    # Rotation matrices
    Ry = np.array([
        [ math.cos(yaw), 0, math.sin(yaw)],
        [ 0,             1, 0           ],
        [-math.sin(yaw), 0, math.cos(yaw)]
    ])

    Rx = np.array([
        [1, 0,              0           ],
        [0, math.cos(pitch), -math.sin(pitch)],
        [0, math.sin(pitch),  math.cos(pitch)]
    ])

    # Combined camera rotation
    R = Rx @ Ry

    # Transform the point into camera space
    rel_pos = np.array([x, y, z])
    cam_space = R @ rel_pos

    # If the point is behind the camera, skip
    if cam_space[2] >= 0:
        return None

    # Project using pinhole camera model
    u = (cam_space[0] * f / -cam_space[2]) + cx
    v = (cam_space[1] * f / -cam_space[2]) + cy  # +cy because Y-axis goes down in image coords

    # Flip Y because in image space (0,0) is top-left
    v = image_size - v

    # Clamp or optionally discard points outside screen
    if u < 0 or u > image_size or v < 0 or v > image_size:
        return None  # block is offscreen

    return (u, v)






print(project_block_to_image(1, -1, 5))