from machine import Pin
from time import sleep_ms

def blink_led(pin):
    led = Pin(pin, Pin.OUT)
    for i in range(10):
        led.on()
        sleep_ms(200)
        led.off()
        sleep_ms(200)

blink_led(5)


def fade_led(pin):
    led = PWM(Pin(pin))
    for i in range(1024):
        led.duty(i)
        time.sleep(0.01)
