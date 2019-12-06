


class Pin():

    def __init__(self, pin = None, pin_mode = None):
        self.pin = pin
        self._val= 0

        self.OUT = None
        self.IN = None
        self.IRQ_FALLING = None
        self.IRQ_RISING  = None


    def value(self, val = None):
        if val == None:
            return self._val
        else:
            if val in (0,1):
                self._val = val
                return self._val
        raise ValueError ('value must be 0 or 1')

    def irq(self, handler=None, trigger=None, *, priority=1, wake=None, hard=False):
        self._handler = handler
        self._trigger = False

    def __trigger_irq(self):
        self._trigger(self.pin)

Pin.IN = None
Pin.OUT = None


class PWM():
    def __init__(self, pin, freq=1000, duty=0):
        self.pin      = pin
        self.pin_no   = pin.pin
        self.freq     = freq
        self.duty_val = duty

    def duty(self, val = None):
        if val == None:
            return self.duty_val
        if 0<= val <= 1023:
            self.duty_val = val
        else:
            raise ValueError ('value must be between 0 and 1023')
