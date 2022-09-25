from microbit import *

while True:
    if pin0.read_digital():
        for x in range(4):
            display.show(Image.HAPPY)
            sleep(1000)
    else:
        display.clear()
    sleep(500)
