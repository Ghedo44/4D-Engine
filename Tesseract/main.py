import pygame as pg
import numpy as np

from tesseract import Tesseract
from matrix_transformation import *
from projection import Projection

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1080
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES, pg.RESIZABLE)
        self.clock = pg.time.Clock()

        self.COLOUR1 = (76, 58, 81)
        self.COLOUR2 = (231, 171, 121)
        self.COLOUR3 = (255, 255, 255)

        self.angle = 0
        self.speed = 0.01

        self.tesseract = Tesseract(self.screen, self.COLOUR2, self.COLOUR3)

    def draw(self):
        self.screen.fill(pg.Color(self.COLOUR1))
        pg.display.set_caption("FPS: " + str(self.clock.get_fps()))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            w, h = pg.display.get_surface().get_size()
            cube_position = [w//2, h//2]
            scale = 4000 / ((self.WIDTH/w + self.HEIGHT/h)/2)

            index = 0

            points = self.tesseract.vertices()
            projected_points = [j for j in range(len(points))]

            for point in points:

                rotated_3d = np.dot(rotation4d_xy(self.angle), point.reshape((4, 1)))
                rotated_3d = np.dot(rotation4d_zw(self.angle), rotated_3d)

                projection = Projection(rotated_3d)


                projected_3d = np.dot(projection.projection_matrix4, rotated_3d)


                rotated_2d = np.dot(rotation_x(self.angle), projected_3d)
                projected_2d = np.dot(projection.projection_matrix, rotated_2d)
                
                x = int(projected_2d[0][0] * scale) + cube_position[0]
                y = int(projected_2d[1][0] * scale) + cube_position[1]

                projected_points[index] = [x, y]

                self.tesseract.draw_points(x, y)
                index += 1

            self.tesseract.draw_edges(projected_points)

            self.angle += self.speed

            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()