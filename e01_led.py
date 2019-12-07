from machine import Pin, PWM
from time import sleep_ms

def blink_led(pin=5):
    led = Pin(pin, Pin.OUT)
    for i in range(10):
        led.on()
        sleep_ms(200)
        led.off()
        sleep_ms(200)



def fade_led(pin=5):
    led = PWM(Pin(pin))
    for i in range(1024):
        led.duty(i)
        sleep_ms(2)
    for i in range(1023, -1, -1):
        led.duty(i)
        sleep_ms(2)
