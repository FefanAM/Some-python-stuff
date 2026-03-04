import math

import pygame
import numpy as np

pygame.init()
width = 1280
height = 720
alpha = beta = gam = 0
dt = 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('3D Cube')
running = True

project = np.array([[1, 0, 0], [0, 1, 0]])

size = 100
radius = 0


class Point:
    def __init__(self, x, y, z, index, color='white'):
        self.coordinates = np.array([[x], [y], [z]])
        self.color = color
        self.z = z
        self.index = index

    def update(self):
        self.z = self.coordinates.ravel()[2]


points = [
    Point(size, size, size, 0),
    Point(size, -size, size, 1),
    Point(-size, -size, size, 2),
    Point(-size, size, size, 3),
    Point(size, size, -size, 4),
    Point(size, -size, -size, 5),
    Point(-size, -size, -size, 6),
    Point(-size, size, -size, 7)
]

lines = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
faces = ((0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (3, 7, 6, 2), (1, 5, 6, 2), (0, 4, 7, 3))
colors = ['red', 'orange', 'blue', 'green', 'white', 'yellow']


def con(coordinates):
    return [coordinates[0] + width // 2, height // 2 - coordinates[1]]


def rotate_x(point, angle):
    rotation = np.array(
        [[1, 0, 0],
         [0, math.cos(angle), - math.sin(angle)],
         [0, math.sin(angle), math.cos(angle)]]
    )
    return np.matmul(rotation, point)


def rotate_y(point, angle):
    rotation = np.array(
        [[math.cos(angle), 0, math.sin(angle)],
         [0, 1, 0],
         [- math.sin(angle), 0, math.cos(angle)]]
    )
    return np.matmul(rotation, point)


def rotate_z(point, angle):
    rotation = np.array(
        [[math.cos(angle), - math.sin(angle), 0],
         [math.sin(angle), math.cos(angle), 0],
         [0, 0, 1]]
    )
    return np.matmul(rotation, point)


def to_2d(point):
    return con(np.matmul(project, point).ravel())


def draw_lines():
    for i in lines:
        a, b = i
        pygame.draw.line(screen, 'white', to_2d(points[a].coordinates), to_2d(points[b].coordinates))


def draw_points():
    for p in points:
        p.coordinates = rotate_x(rotate_y(rotate_z(p.coordinates, gam), beta), alpha)
        p.update()
        pygame.draw.circle(screen, 'white', to_2d(p.coordinates), radius)


def draw_faces():
    face_order = points.copy()
    face_order.sort(key=lambda x: x.z, reverse=True)
    # for j in range(len(face_order) - 1):
    for i, color in zip(faces, colors):
        if face_order[0].index in i:
            a, b, c, d = i
            pygame.draw.polygon(screen, color, [to_2d(points[a].coordinates), to_2d(points[b].coordinates), to_2d(points[c].coordinates), to_2d(points[d].coordinates)])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    mouse_x, mouse_y = pygame.mouse.get_rel()

    if pygame.mouse.get_pressed()[2]:
        alpha += mouse_y / (height + width) * 8
        beta += mouse_x / (height + width) * 8

    draw_points()

    # draw_lines()

    draw_faces()

    alpha = beta = 0
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
