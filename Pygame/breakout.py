import math

import pygame
import random

# pygame setup
pygame.init()
width = 1330
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
all_sprites_list = pygame.sprite.Group()
dt = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, n, m):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        block_width = 100
        block_height = 30
        colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
        if m >= len(colors):
            c = m - len(colors)
        else:
            c = m
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(colors[c])

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = 10 + n * (block_width + 10)
        self.rect.y = 10 + m * (block_height + 5)


class Ball(pygame.sprite.Sprite):
    def __init__(self, size, speed):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.size = size
        self.angle = 45
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'white', (self.size // 2, self.size // 2), self.size // 2)
        self.image = self.image.convert_alpha()
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.size // 2
        self.rect.y = height // 2 + 200

    def move(self):
        self.x += math.cos(self.angle) * self.speed * dt
        self.y -= math.sin(self.angle) * self.speed * dt

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = min(max(0, value), width - self.size)

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = min(max(0, value), height - self.size)

    @property
    def phi(self):
        return self.angle

    @phi.setter
    def phi(self, ang):
        self.angle = ang


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.width = 100
        self.image = pygame.Surface([self.width, 30])
        self.image.fill('white')
        self.speed = 1000

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.width // 2
        self.rect.y = height - 50

    def left(self):
        self.x -= self.speed * dt

    def right(self):
        self.x += self.speed * dt

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = min(max(0, value), width - self.width)


for y in range(int((height / 2) / 30)):
    for x in range(int(width / 100)):
        all_sprites_list.add((Block(x, y)))

player = Player()
all_sprites_list.add(player)

ball = Ball(30, 1000)
all_sprites_list.add(ball)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.left()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.right()
    if keys[pygame.K_e]:
        ball.phi += 10 * dt
    if keys[pygame.K_r]:
        ball.phi -= 10 * dt
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    ball.move()
    all_sprites_list.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()