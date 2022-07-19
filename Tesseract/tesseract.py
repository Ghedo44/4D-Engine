from turtle import color
import numpy as np
import pygame as pg
import random

class Tesseract:
    def __init__(self, render, point_color, edge_color):
        self.render = render
        self.point_color = point_color
        self.edge_color = edge_color

        self.color = []
        for _ in range(16):
            self.color.append(tuple(map(lambda a : a * random.randint(0, 255), [1,1,1])))
        

    def vertices(self):
        points = []

        # all the cube vertices
        points.append(np.matrix([-1, -1, 1, 1]))
        points.append(np.matrix([1, -1, 1, 1]))
        points.append(np.matrix([1,  1, 1, 1]))
        points.append(np.matrix([-1, 1, 1, 1]))
        points.append(np.matrix([-1, -1, -1, 1]))
        points.append(np.matrix([1, -1, -1, 1]))
        points.append(np.matrix([1, 1, -1, 1]))
        points.append(np.matrix([-1, 1, -1, 1]))
        points.append(np.matrix([-1, -1, 1, -1]))
        points.append(np.matrix([1, -1, 1, -1]))
        points.append(np.matrix([1,  1, 1, -1]))
        points.append(np.matrix([-1, 1, 1, -1]))
        points.append(np.matrix([-1, -1, -1, -1]))
        points.append(np.matrix([1, -1, -1, -1]))
        points.append(np.matrix([1, 1, -1, -1]))
        points.append(np.matrix([-1, 1, -1, -1]))

        return points

        

    def connect_point(self, i, j, k, offset):
        a = k[i + offset]
        b = k[j + offset]
        pg.draw.line(self.render, self.edge_color, (a[0], a[1]), (b[0], b[1]), 3)

    #draw edges
    def draw_edges(self, projected_points):
        for m in range(4):
            self.connect_point(m, (m+1)%4, projected_points, 8)
            self.connect_point(m+4, (m+1)%4 + 4, projected_points, 8)
            self.connect_point(m, m+4, projected_points, 8, )

        for m in range(4):
            self.connect_point(m, (m+1)%4, projected_points, 0)
            self.connect_point(m+4, (m+1)%4 + 4, projected_points, 0)
            self.connect_point(m, m+4, projected_points, 0)

        for m in range(8):
            self.connect_point(m,  m+8, projected_points, 0)

    #draw points
    def draw_points(self, x, y, i):
        pg.draw.circle(self.render, self.color[i], (x, y), 10)

if __name__ == '__main__':
    print('c')