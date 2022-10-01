# https://makecode.microbit.org/

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        serial.write_string("s")


basic.forever(on_forever)
