import pygame as pg
import numpy as np
import tkinter as tk

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

        self.done = False

        #initialise tkinter
        root = tk.Tk()
        self.main_dialog =  tk.Frame(root)
        root.protocol("WM_DELETE_WINDOW", self.quit_callback)
        self.main_dialog.pack()

        self.xrot = tk.IntVar()
        self.yrot = tk.IntVar()
        self.zrot = tk.IntVar()

        self.cxrot = tk.Checkbutton(self.main_dialog, text='Rotation 3D X plane',variable=self.xrot, onvalue=0, offvalue=1)
        self.cxrot.pack()
        self.cyrot = tk.Checkbutton(self.main_dialog, text='Rotation 3D Y plane',variable=self.yrot, onvalue=1, offvalue=0)
        self.cyrot.pack()
        self.czrot = tk.Checkbutton(self.main_dialog, text='Rotation 3D Z plane',variable=self.zrot, onvalue=1, offvalue=0)
        self.czrot.pack()

        self.zwrot = tk.IntVar()
        self.xyrot = tk.IntVar()
        self.xzrot = tk.IntVar()
        self.xwrot = tk.IntVar()
        self.yzrot = tk.IntVar()
        self.ywrot = tk.IntVar()

        self.czwrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D ZW plane',variable=self.zwrot, onvalue=0, offvalue=1)
        self.czwrot.pack()
        self.cxyrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D XY plane',variable=self.xyrot, onvalue=0, offvalue=1)
        self.cxyrot.pack()
        self.cxzrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D XZ plane',variable=self.xzrot, onvalue=1, offvalue=0)
        self.cxzrot.pack()
        self.cxwrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D XW plane',variable=self.xwrot, onvalue=1, offvalue=0)
        self.cxwrot.pack()
        self.cyzrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D XZ plane',variable=self.yzrot, onvalue=1, offvalue=0)
        self.cyzrot.pack()
        self.cywrot = tk.Checkbutton(self.main_dialog, text='Rotation 4D XW plane',variable=self.ywrot, onvalue=1, offvalue=0)
        self.cywrot.pack()

    def quit_callback(self):
        self.done = True

    def draw(self):
        self.screen.fill(pg.Color(self.COLOUR1))
        pg.display.set_caption("FPS: " + str(self.clock.get_fps()))
        self.main_dialog.update()


    def run(self):
        while not self.done:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]


            

            w, h = pg.display.get_surface().get_size()
            cube_position = [w//2, h//2]
            scale = 4000 / ((self.WIDTH/w + self.HEIGHT/h)/2)

            index = 0

            points = self.tesseract.vertices()
            projected_points = [j for j in range(len(points))]

            for point in points:

                rotated_3d = point.reshape((4, 1))

                if self.xyrot.get() == 0:
                    rotated_3d = np.dot(rotation4d_xy(self.angle), rotated_3d)

                if self.zwrot.get() == 0:
                    rotated_3d = np.dot(rotation4d_zw(self.angle), rotated_3d)

                if self.xzrot.get() == 1:
                    rotated_3d = np.dot(rotation4d_xz(self.angle), rotated_3d)
                
                if self.xwrot.get() == 1:
                    rotated_3d = np.dot(rotation4d_xw(self.angle), rotated_3d)

                if self.yzrot.get() == 1:
                    rotated_3d = np.dot(rotation4d_yz(self.angle), rotated_3d)
                
                if self.ywrot.get() == 1:
                    rotated_3d = np.dot(rotation4d_yw(self.angle), rotated_3d)

                projection = Projection(rotated_3d)


                projected_3d = np.dot(projection.projection_matrix4, rotated_3d)

                rotated_2d = projected_3d
                if self.xrot.get() == 0:
                    rotated_2d = np.dot(rotation_x(self.angle), rotated_2d)
                if self.yrot.get() == 1:
                    rotated_2d = np.dot(rotation_y(self.angle), rotated_2d)
                if self.zrot.get() == 1:
                    rotated_2d = np.dot(rotation_z(self.angle), rotated_2d)


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