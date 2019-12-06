import machine
from umqttsimple import MQTTClient
from time import sleep_ms
import ujson
from urandom import getrandbits

server = '10.0.1.2'
btn = machine.Pin(13, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)

client = MQTTClient(client_id = 'buttonbox', server = server, port = 1883)
client.connect()

def random_color():

    color = {"r": getrandbits(8),
             "g": getrandbits(8),
             "b": getrandbits(8)
            }
    c = 4
    while c >= 3:
        c = getrandbits(2)
    c = ("r","g","b")[c]
    color[c] = 0

    return {"color":color, "state": "ON", "brightness" : 255}

def button_pushed():
    global led
    global mqtt_client
    topic = 'buttonbox/set'

    print("button pushed")
    if led.value() == 1:
        led.value(0)
#        state = 'OFF'
    elif led.value() == 0:
        led.value(1)
#        state = 'ON'
    state = ujson.dumps(random_color())
    client.publish(topic.encode('UTF-8'),
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

run_btn()
