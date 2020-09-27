import pygame
from random import random
from math import sqrt

SCREEN_SIZE = (1280, 720)
class Vector:
    def __init__(self, x, y, vec):
        self.x = x
        self.y = y
        self.vec = vec

    def __sub__(self, y):  # разность векторов
        return self.x[0] - self.y[0], self.x[1] - self.y[1]

    def __add__(self, y):  # сумма векторов
        return self.x[0] + self.y[0], self.x[1] + self.y[1]

    def length(self):  # длинна вектора
        return sqrt(self.x[0] * self.x[0] + self.x[1] * self.x[1])

    def multiply(vec, k):  # умножение вектора на число
        return vec.vec[0] * k, vec.vec[1] * k

    def scalar_multiply(vec, k):  # скалярное умножение векторов
        return vec.vec[0] * k, vec.vec[1] * k


    def vector(x, y):  # создание вектора по началу (x) и концу (y) направленного отрезка
        return __sub__(y, x)

class Line:

    def __init__(self, points, style, width, color):
        self.points = points
        self.style = style
        self.width = width
        self.color = color

    def draw_points(self, points, style="points", width=4, color=(255, 255, 255)):
        if style == "line":
            for point_number in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color, (int(points[point_number][0]), int(points[point_number][1])),
                                 (int(points[point_number + 1][0]), int(points[point_number + 1][1])), width)

        elif style == "points":
            for point in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(point[0]), int(point[1])), width)

