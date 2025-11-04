import time

rise = True
running = True
width = 120
height = 29


def clear_all():
    for a in range(height + 1):
        print(" ")


while running:
    for x in range(height):
        if x == 0:
            print("▨" + "≡" * 118 + "▧")
        elif x == height - 1:
            print("▧" + "≡" * 118 + "▨")
        else:
            print("|" + 118 * " " + "|")
    time.sleep(0.0183)
    clear_all()
