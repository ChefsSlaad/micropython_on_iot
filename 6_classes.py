from machine import Pin, PWM, Timer
from time import time sleep_ms


class OutputDevice():
    '''
    OutputDevice is a generic GPIO output device.

    this class defines common methods for GPIO devices:
    an :meth: 'on' method to switch the device on, a corresponding
    :meth: 'off' method and a :meth: 'toggle' method
    :meth: 'value()' returns the current state of the device
    :meth: 'value([int])' sets the state of the device

    :type pin: int
    :param pin:
      the GPIO pin that the device is connected to. In the current
      implementation on esp8266, only pins 0,2,4,5,12,13,14,15 and 16
      are valid pins
      if this is not a valid pin, a :exc: 'ValueError' will be raised

    :param bool active_high:
        If :data:`True` (the default), the :meth:`on` method will set the GPIO
        to HIGH. If :data:`False`, the :meth:`on` method will set the GPIO to
        LOW (the :meth:`off` method always does the opposite).

    :type start_on: bool
    :param start_on:
        If :data:`False` (the default), the device will be off initially. If
        :data:`True`, the device will be switched on initially.
    '''
    def __init__(self, pin, inverted = False, start_on = False):
        if pin not in (0, 2, 4, 5, 12, 13, 14, 15,):
            raise ValueError ("pin must be 0, 2, 4, 5, 12, 13, 14, or 15")
        self.pin = pin
        self.inverted = inverted

        self._output_device = Pin(pin, Pin.OUT)
        self._val = None
        self.isOn = None

        if start_on:
            self.value(1)
        else:
            self.value(0)

    def __repr__(self):
        return "<micro_gpio.{}> object on pin {}, inverted {}, isOn {}".format(
                self.__class__.__name__, self.pin, self.inverted, self.isOn)

    def _write(self, value):
        self._output_device.value(value)

    def value(self, value = None):
        if value == None:
           return self._val
        assert value in (0,1), "this device must be set to either 0 or 1, but value  {}  was given".format(value)
        self.isOn = value == 1
        self._val = value
        if self.inverted:
           value = 1-value # invert value if the led is inverted
        self._write(value)

    def on(self):
        self.value(1)

    def off(self):
        self.value(0)

    def toggle():
        if self.ison:
            self.off()
        else:
            self.on()

class LED(OutputDevice):
    def blink(self, blinks = 0, wait_ms = 1000, background = True):
        self.blinks = blinks
        self.blink = 0
        self.wait_ms = wait_ms
        self.background = background
        self.timer = Timer()

        self._start_blink()

    def _blink_background(self):
        self.blink += 1
        self.toggle()
        if self.blink >= self.blinks:
            self._stop_blink()

    def _start_blink(self):
        if self.background
            self.timer.init(period = self.wait_ms, callback = self._blink_background)
        else:
            for i in range(blinks):
                self.toggle()
                sleep_ms(self.wait_ms)

    def _stop_blink(self):
        timer.deinit()
