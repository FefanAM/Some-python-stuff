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
running = True

project = np.array([[1, 0, 0], [0, 1, 0]])

points = [
    np.array([[50], [50], [50]]),
    np.array([[50], [-50], [50]]),
    np.array([[-50], [50], [50]]),
    np.array([[-50], [-50], [50]]),
    np.array([[50], [50], [-50]]),
    np.array([[50], [-50], [-50]]),
    np.array([[-50], [50], [-50]]),
    np.array([[-50], [-50], [-50]])
]


def connect_dots(dots):
    for dot in dots:
        for d in dots:
            if dot.ravel()[0] == d.ravel()[0] and dot.ravel()[1] == d.ravel()[1] or dot.ravel()[0] == d.ravel()[0] and dot.ravel()[2] == d.ravel()[2] or dot.ravel()[2] == d.ravel()[2] and dot.ravel()[1] == d.ravel()[1]:
                pygame.draw.line(screen, 'white', to_2d(dot), to_2d(d))


def c(coordinates):
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
         [ 0, 0, 1]]
    )
    return np.matmul(rotation, point)


def rotate_somehow(point, angle):
    rotation = np.array(
        [[math.cos(angle), - math.sin(angle), 0],
         [math.sin(angle), 1, math.cos(angle)],
         [ 0, 0, 1]]
    )
    return np.matmul(rotation, point)



def to_2d(point):
    return c(np.matmul(project, point).ravel())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    points_lines = []

    for p in points:
        p = rotate_x(rotate_y(rotate_z(p, gam), beta), alpha)
        points_lines.append(p)
        pygame.draw.circle(screen, 'white', to_2d(p), 20)

    connect_dots(points_lines)

    pygame.display.flip()
    alpha += 3 * dt
    beta += 2 * dt
    gam += 1 * dt
    dt = clock.tick(60) / 1000

pygame.quit()
