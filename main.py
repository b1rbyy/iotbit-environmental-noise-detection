OLED.init(128, 64)

def on_forever():
    OLED.clear()
    OLED.draw_loading(Environment.read_noise(AnalogPin.P1))
    basic.pause(50)
basic.forever(on_forever)
