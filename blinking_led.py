import machine
from time import sleep

def blink_led(pin):
    led = machine.Pin(pin, machine.Pin.OUT)
    for i in range(10):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)

if __name__ == '__main__':
    blink_led(2)
