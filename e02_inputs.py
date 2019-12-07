from machine import Pin, PWM
from time import sleep_ms
import dht


def button_pushed(p):
    global led
    print("button on pin {} pushed".format(p))
    if led.value() == 1:
        led.value(0)
    elif led.value() == 0:
        led.value(1)

def button():
    global led
    global btn
    btn = Pin(14, Pin.IN)
    led = Pin(5,  Pin.OUT)
    btn.irq(handler = button_pushed, trigger = Pin.IRQ_FALLING)


def tilt_sensor():
    tilt = Pin(4, Pin.IN)
    tilt.irq(handler = lambda p: print('tilt'), tirgger = Pin.IRQ_FALLING)


def temp_humid():
    sensor = dht.DHT11(Pin(0))
    while True:
        sensor.measure()
        print('temperature {:>2}c    humidity {:>2}%'.format(
                        sensor.temperature(), sensor.humidity()))
        sleep_ms(1000)
