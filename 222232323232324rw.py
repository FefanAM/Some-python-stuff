import time
import keyboard
import random
import os

running = True
width = 120
height = 29
speed = 0.25
fruit_count = 10
facing = 'east'
game_contents = [[], []]  # stores all objects currently in game -- used for rendering -- list 0 is player -- list 1 is fruits
current_row = []


class GameObject:
    def __init__(self, name, pos_x, pos_y, char):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.char = char


def clear_all():
    # clear the terminal screen
    for a in range(height + 1):
        print(" ")


def print_row(current_y):
    # loop through every object in game contents and add them to currently printed row
    global current_row
    current_row.clear()
    for x in range(width - 2):
        current_row.append(" ")
    for group in game_contents:
        for item in group:
            if item.pos_y // 1 == current_y:
                current_row.pop(int(item.pos_x // 1))
                current_row.insert(int(item.pos_x // 1), item.char)


def new_frame():
    # print a new frame in terminal
    for x in range(height):
        if x == 0:
            print("▨" + "≡" * (width - 2) + "▧")
        elif x == height - 1:
            print("▧" + "≡" * (width - 2) + "▨")
        else:
            print_row(x)
            print("|" + "".join(map(str, current_row)) + "|")


def move_player():
    # set the facing direction via key input
    global facing
    if keyboard.is_pressed('w') and facing != 'south':
        facing = 'north'
    elif keyboard.is_pressed('s') and facing != 'north':
        facing = 'south'
    elif keyboard.is_pressed('a') and facing != 'east':
        facing = 'west'
    elif keyboard.is_pressed('d') and facing != 'west':
        facing = 'east'
    # move the player in right direction
    if facing == 'north':
        game_contents[0][0].pos_y -= speed / 2
    if facing == 'south':
        game_contents[0][0].pos_y += speed / 2
    if facing == 'west':
        game_contents[0][0].pos_x -= speed
    if facing == 'east':
        game_contents[0][0].pos_x += speed
    # make sure player cannot get out of bounds
    if game_contents[0][0].pos_x >= width - 3:
        game_contents[0][0].pos_x = width - 3
    if game_contents[0][0].pos_x <= 0:
        game_contents[0][0].pos_x = 0
    if game_contents[0][0].pos_y >= height - 2:
        game_contents[0][0].pos_y = height - 2
    if game_contents[0][0].pos_y <= 1:
        game_contents[0][0].pos_y = 1


def place_fruits():
    # if number of fruits is less than is set, add a new fruit
    while len(game_contents[1]) < fruit_count:
        game_contents[1].append(GameObject('fruit', random.randrange(0, width - 3), random.randrange(1, height - 2), '∘'))


def eat_fruit():
    for fruit in game_contents[1]:
        if fruit.pos_y == game_contents[0][0].pos_y // 1 and fruit.pos_x == game_contents[0][0].pos_x // 1:
            del game_contents[1][game_contents[1].index(fruit)]


game_contents[0].append(GameObject('player', width // 2, height // 2, '■'))

while running:
    place_fruits()
    new_frame()
    time.sleep(0.01)
    os.system('cls')
    # clear_all()
    move_player()
    eat_fruit()
