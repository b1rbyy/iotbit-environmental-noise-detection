OLED.init(128, 64)
basic.forever(function () {
    OLED.clear()
    OLED.drawLoading(Environment.ReadNoise(AnalogPin.P1))
})
