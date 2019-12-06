import machine
from umqtt.simple import MQTTClient

server = '10.0.1.2'
led1 = machine.PWM(machine.Pin(15))
led2 = machine.PWM(machine.Pin(13))
led3 = machine.PWM(machine.Pin(12))
led4 = machine.PWM(machine.Pin(14))

mqtt_client = MQTTClient(client_id = 'lightbox', server = server, port = 1883)
mqtt_client.connect()

def on_message(topic, message):
    topic   = topic.decode('UTF-8')
    message = message.decode('UTF-8')
    print('recieved {} from {}.format(message, topic) )
    if message == "ON":
        led1.duty(1023)

mqtt_client.set_callback(on_message)

while True:
    mqtt_client.wait_msg()
