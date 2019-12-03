From machine import Pin, PWM
From time import sleep

def fade_led(pin):
    led = machine.PWM(machine.Pin(pin))
    for i in range(1024):
        led.duty(i)
        time.sleep(0.01)

if __name__ == '__main__':
    fade_led(2)
