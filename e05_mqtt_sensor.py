import machine
from umqtt.simple import MQTTClient
from time import sleep_ms

server = '10.0.1.1'
btn = machine.Pin(13, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)

mqtt_client = MQTTClient(client_id = 'buttonbox', server = server, port = 1883)
mqtt_client.connect()

def button_pushed():
    global led
    global mqtt_client
    topic = 'buttonbox/state'

    print("button pushed")
    if led.value() == 1:
        led.value(0)
        state = 'OFF'
    elif led.value() == 0:
        led.value(1)
        state = 'ON'
    mqtt_client.publish( topic.encode('UTF-8'),
                         state.encode('UTF-8'))

def run_btn(interval=10, precision = 25, callback=button_pushed):
    counter = 0
    while True:
        if btn.value() == 1:
            counter +=1
        elif counter > 0 and btn.value() == 0:
            counter -=0

        if counter > precision:
            counter = 0
            callback()
        sleep_ms(interval)
