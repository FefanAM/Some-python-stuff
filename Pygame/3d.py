import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

project = np.array([[1, 0, 0], [0, 1, 0]])
point1 = np.array([[50], [50], [0]])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, 'white', np.matmul(project, point1).ravel(), 20)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
