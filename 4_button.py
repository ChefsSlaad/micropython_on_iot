import machine

def button_pushed(p):
    global led
    print("button on pin {} pushed".format(p))
    if led.value() == 1:
        led.value(0)
    elif led.value() == 0:
        led.value(1)

if __name__ == '__main__':
    btn = machine.Pin(15, machine.Pin.IN)
    led = machine.Pin(13, machine.Pin.OUT)
    btn.irq(handler = button_pushed, trigger = led.IRQ_RISING)
