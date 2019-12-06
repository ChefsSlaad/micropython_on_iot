import machine
from umqttsimple import MQTTClient
from led_devices import led_strip

server = '10.0.1.2'
topic = b'buttonbox/state'

config = {"type": "led_strip",
          "state_topic":   "buttonbox",
          "command_topic": "buttonbox/set",
          "pin": {
            "red":   12,
            "green": 15,
            "blue":  13
          }
      }

leds = led_strip(config)

def on_message(topic, message):
    topic   = topic.decode('UTF-8')
    message = message.decode('UTF-8')
    print('recieved:', message)
    leds.update(message)


mqtt_client = MQTTClient(client_id = 'lightbox', server = server, port = 1883)
mqtt_client.set_callback(on_message)
mqtt_client.connect()
mqtt_client.subscribe(config['command_topic'].encode('utf-8'))


while True:
    mqtt_client.wait_msg()
    print(leds)
