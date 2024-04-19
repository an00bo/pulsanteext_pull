stato = 0

def on_forever():
    global stato
    if pins.digital_read_pin(DigitalPin.P0) == 1 and stato == 0:
        basic.show_icon(IconNames.YES)
        stato = 1
    if pins.digital_read_pin(DigitalPin.P0) == 1 and stato == 1:
        basic.show_icon(IconNames.NO)
        stato = 0
basic.forever(on_forever)
