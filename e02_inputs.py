from machine import Pin
from time import sleep_ms
import dht


def button_pushed(p):
    global led
    print("button on pin {} pushed".format(p))
    if led.value() == 1:
        led.value(0)
    elif led.value() == 0:
        led.value(1)

btn = Pin(14, Pin.IN)
led = Pin(5,  Pin.OUT)
btn.irq(handler = button_pushed, trigger = Pin.IRQ_FALLING)


tilt = Pin(4, Pin.IN)
til.irq(lambda p: print('tilt'), tirgger = Pin.IRQ_FALLING)



th_sensor = dht.DHT11(Pin(0))
def temp_humid(sensor = th_sensor):
    while True:
        sensor.measure()
        print('temperature {:>2}c    humidity {:>2}%'.format(
                        sensor.temperature(), sensor.humidity()))
        sleep_ms(1000)
