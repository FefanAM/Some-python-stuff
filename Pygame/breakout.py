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


class Player(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([100, 30])
        self.image.fill('white')

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - 50
        self.rect.y = height - 50


for y in range(int((height / 2) / 30)):
    for x in range(int(width / 100)):
        all_sprites_list.add((Block(x, y)))

all_sprites_list.add(Player())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    all_sprites_list.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()