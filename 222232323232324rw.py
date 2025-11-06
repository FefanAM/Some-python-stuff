import time

running = True
width = 120
height = 29
game_contents = []
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
    for item in game_contents:
        if item.pos_y == current_y:
            current_row.pop(item.pos_x)
            current_row.insert(item.pos_x, item.char)


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


game_contents.append(GameObject('block', 58, 10, '0'))

while running:
    new_frame()
    time.sleep(0.0183)
    clear_all()
    if game_contents[0].pos_x == 117:
        game_contents[0].pos_x = 0
        game_contents[0].pos_y += 1
    else:
        game_contents[0].pos_x += 1
