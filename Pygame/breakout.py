import math
import pygame

# pygame setup
pygame.init()
width = 1330
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Breakout')
clock = pygame.time.Clock()
running = True
block_list = pygame.sprite.Group()
balls = pygame.sprite.Group()
dt = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, n, m, health):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.width = 100
        self.height = 30
        self.hp = health
        colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
        if m >= len(colors):
            c = m - len(colors)
        else:
            c = m
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(colors[c])

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = 10 + n * (self.width + 10)
        self.rect.y = 10 + m * (self.height + 5)

    def damage(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()
            blocks.remove(self)

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y


class Ball(pygame.sprite.Sprite):
    def __init__(self, size, speed, angle):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.size = size
        self.angle = angle
        self.bx = self.by = 1
        self.padding = 5
        self.image = pygame.Surface([self.size, self.size], pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'white', (self.size // 2, self.size // 2), self.size // 2)
        self.image = self.image.convert_alpha()
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.center()

    def center(self):
        self.rect.x = width // 2 - self.size // 2
        self.rect.y = height // 2 + 200

    def move(self):
        self.x += math.cos(self.angle) * self.speed * dt * self.bx
        self.y -= math.sin(self.angle) * self.speed * dt * self.by

    def collision(self, col):
        if self.x == 0 or self.x == width - self.size:
            self.bx *= -1
        if self.y == 0:
            self.by *= -1

        collisions = self.rect.collideobjectsall(col)
        for c in collisions:
            if isinstance(c, Player):
                self.by *= -1
                self.y = c.y - self.size
                return
            if c.x + c.width > self.x + self.padding > c.x or c.x + c.width > self.x + self.size - self.padding > c.x:
                self.by *= -1
            elif c.y + c.height > self.y + self.padding > c.y or c.y + c.height > self.y + self.size - self.padding > c.y:
                self.bx *= -1
            if isinstance(c, Block):
                c.damage()
            return

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
        if self.y == height - self.size:
            self.center()

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

        self.width = 200
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill('white')
        self.speed = 1000

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.width // 2
        self.rect.y = height - 100

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

    @property
    def y(self):
        return self.rect.y


blocks = []
for y in range(int((height / 2) / 30)):
    for x in range(int(width / 100)):
        blocks.append((Block(x, y, 1)))

player = Player()
blocks.append(player)
block_list.add(blocks)

ball = Ball(30, 600, 45)
balls.add(ball)

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
    for ball in balls:
        ball.move()
        ball.collision(blocks)
    block_list.draw(screen)
    balls.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(400) / 1000

pygame.quit()
