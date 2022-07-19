import math
from tkinter import Y
import numpy as np


class Projection:
    def __init__(self, rotated_3d, x, y, z):
        DISTANCE = 5.4

        x = math.radians(x)
        y = math.radians(y)
        z = math.radians(z)

        # 'rotazione della camera'
        TESSERACT_ROTATION =  np.array( 
            [
                [1, 0, 0],
                [0, math.cos(-x), -math.sin(-x)],
                [0, math.sin(-x), math.cos(-x)]
            ])
        
        TESSERACT_ROTATIONY =  np.array( 
            [
                [math.cos(y), 0, -math.sin(y)],
                [0, 1, 0],
                [math.sin(y), 0, math.cos(y)]
            ])
        
        TESSERACT_ROTATIONZ =  np.array( 
            [
                [math.cos(z), -math.sin(z), 0],
                [math.sin(z), math.cos(z), 0],
                [0, 0 ,1]
            ])

        #print(rotated_3d)
        #print('\n\n')
        w = 1/(DISTANCE - rotated_3d[3][0])
        self.projection_matrix4 = np.array(
            [
                [w, 0, 0, 0],
                [0, w, 0, 0],
                [0, 0, w, 0],
            ])


        projected_3d = np.dot(self.projection_matrix4, rotated_3d)
        rotated_2d = np.dot(TESSERACT_ROTATION, projected_3d)
        rotated_2d = np.dot(TESSERACT_ROTATIONY, rotated_2d)
        rotated_2d = np.dot(TESSERACT_ROTATIONZ, rotated_2d)

        z = 1/(DISTANCE - (rotated_2d[2][0]+ rotated_3d[3][0]))
        
        self.projection_matrix = np.array(
            [
                [z, 0, 0],
                [0, z, 0 ]
            ]
        )