import unittest

class led_tests(unittest.TestCase):
    def setUp(self):

        self.single_led = led_devices.led_pwm_simple(led_config)

    def tearDown(self):
        pass

    def test_led_init(self):
        led = self.single_led
        self.assertEqual(led.val, 0, 'led_pwm.val is not 0')
        self.assertEqual(led.type, 'led', 'led_pwm.type is not "led"')
        self.assertEqual(led.state, 'OFF', 'led_pwm.state is not "OFF"')
        self.assertEqual(led.is_on, False, 'led_pwm.is_on is not False')
        self.assertEqual(led.topic, led_config["state_topic"], 'led_pwm.topic is not correct')
        self.assertEqual(led.set_topic, led_config["command_topic"], 'led_pwm.set_topic is not correct')
        self.assertEqual(led.inverted, False, 'led_pwm.inverted is not False')

    def test_led_print(self):
        expectedstring = "is_on: False, inverted: False, value: 0, duty: 0"
        self.assertEqual(self.single_led.__str__(), expectedstring)

    def test_led_read_value(self):
        v = 0
        self.assertEqual(self.single_led.value(), v, msg='value() does not return {}'.format(v))

    def test_led_set_value(self):
        for v in range(256):
            self.assertEqual(self.single_led.value(v), v, msg='value() does not return {}'.format(v))
