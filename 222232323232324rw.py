import time
rise = True

wave = "|"
while True:
    if len(wave) == 20:
        rise = False
    elif len(wave) == 1:
        rise = True
    print(wave)
    if rise:
        wave = wave + "|"
    else:
        wave = "|" * (len(wave) - 1)
    time.sleep(0.1)