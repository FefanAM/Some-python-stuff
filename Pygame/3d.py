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
    np.array([[-50], [-50], [50]]),
    np.array([[-50], [50], [50]]),
    np.array([[50], [50], [-50]]),
    np.array([[50], [-50], [-50]]),
    np.array([[-50], [-50], [-50]]),
    np.array([[-50], [50], [-50]])
]

lines = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))

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

    for i in lines:
        a, b = i
        pygame.draw.line(screen, 'white', to_2d(points_lines[a]), to_2d(points_lines[b]))

    pygame.display.flip()
    alpha += 3 * dt
    beta += 2 * dt
    gam += 1 * dt
    dt = clock.tick(60) / 1000

pygame.quit()
