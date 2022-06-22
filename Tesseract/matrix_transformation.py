import math
import numpy as np

#3d matrix rotations
def rotation_x(angle):
    return np.array(
        [
            [1, 0, 0], 
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)]
        ])

def rotation_y(angle):
    return np.array(
        [
            [math.cos(angle), 0, -math.sin(angle)],
            [0, 1, 0],
            [math.sin(angle), 0, math.cos(angle)]
        ])

def rotation_z(angle):
    return np.array(
        [
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0 ,1]
        ])

        
#4d matrix rotations
def rotation4d_xy(angle):
    return np.array(
        [
            [math.cos(angle), -math.sin(angle), 0, 0],
            [math.sin(angle), math.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

def rotation4d_xz(angle):
    return np.array(
        [
            [math.cos(angle), 0, -math.sin(angle), 0],
            [0, 1, 0, 0],
            [math.sin(angle), 0, math.cos(angle), 0],
            [0, 0, 0, 1]
        ])

def rotation4d_xw(angle):
    return np.array(
        [
            [math.cos(angle), 0, 0, -math.sin(angle)],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [math.sin(angle), 0, 0, math.cos(angle)]
        ])

def rotation4d_yz(angle):
    return np.array(
        [
            [1, 0, 0, 0],
            [0, math.cos(angle), -math.sin(angle), 0],
            [0, math.sin(angle), math.cos(angle), 0],
            [0, 0, 0, 1]
        ])

def rotation4d_yw(angle):
    return np.array(
        [
            [1, 0, 0, 0],
            [0, math.cos(angle), 0, -math.sin(angle)],
            [0, 0, 1, 0],
            [0, math.sin(angle), 0, math.cos(angle)]
        ])

def rotation4d_zw(angle):
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, math.cos(angle), -math.sin(angle)],
            [0, 0, math.sin(angle), math.cos(angle)]
        ])