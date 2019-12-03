import machine
from umqtt.simple import MQTTClient

server = '10.0.1.2'
btn = machine.Pin(15, machine.Pin.IN)
led = machine.Pin(13, machine.Pin.OUT)

mqtt_client = MQTTClient(client_id = 'buttonbox', server = server, port = 1883)
mqtt_client.connect()

def button_pushed(p):
    global led
    global mqtt_client
    print("button on pin {} pushed".format(p))
    if led.value() == 1:
        led.value(0)
        state = 'ON'
    elif led.value() == 0:
        led.value(1)
        state = 'OFF'
    mqtt_client.publish('buttonbox/state'.encode('UTF-8'),
                         state.encode('UTF-8'))

btn.irq(handler = button_pushed, trigger = led.IRQ_RISING)
