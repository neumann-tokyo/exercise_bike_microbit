from pynput.keyboard import Key, Controller
import serial
import time

ser = serial.Serial(
    port="COM3",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=None,
    xonxoff=False
)
keyboard = Controller()

while True:
    line = ser.read()
    command = str(line).lstrip("b'").rstrip("'")

    if (command == "s"):
        print("UP")
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    time.sleep(0.5)
