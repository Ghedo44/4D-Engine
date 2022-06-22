import math
import numpy as np


class Projection:
    def __init__(self, rotated_3d):
        DISTANCE = 5

        # 'rotazione della camera'
        TESSERACT_ROTATION =  np.array( 
            [
                [1, 0, 0],
                [0, math.cos(-math.pi/2), -math.sin(-math.pi/2)],
                [0, math.sin(-math.pi/2), math.cos(-math.pi/2)]
            ])


        w = 1/(DISTANCE - rotated_3d[3][0])
        self.projection_matrix4 = np.array(
            [
                [w, 0, 0, 0],
                [0, w, 0, 0],
                [0, 0, w, 0],
            ])


        projected_3d = np.dot(self.projection_matrix4, rotated_3d)
        rotated_2d = np.dot(TESSERACT_ROTATION, projected_3d)
        z = 1/(DISTANCE - (rotated_2d[2][0] + rotated_3d[3][0]))
        
        self.projection_matrix = np.array(
            [
                [z, 0, 0],
                [0, z, 0 ]
            ]
        )