let stato = 0
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 1 && stato == 0) {
        basic.showIcon(IconNames.Yes)
        stato = 1
    }
    if (pins.digitalReadPin(DigitalPin.P0) == 1 && stato == 1) {
        basic.showIcon(IconNames.No)
        stato = 0
    }
})
