import gpiod
import time

chip = gpiod.Chip('gpiochip0')

def p_on(pin):
    line = chip.get_line(pin)
    config = gpiod.LineRequest()
    config.consumer = 'relay_control'
    config.request_type = gpiod.LineRequest.DIRECTION_OUTPUT
    line.request(config, default_val=0)
    line.set_value(1)
    print(f"Relay on pin {pin} is now ON")

def p_off(pin):
    line = chip.get_line(pin)
    config = gpiod.LineRequest()
    config.consumer = 'relay_control'
    config.request_type = gpiod.LineRequest.DIRECTION_OUTPUT
    line.request(config, default_val=0)
    line.set_value(0)
    print(f"Relay on pin {pin} is now OFF")

def squirt(pin):
    p_on(pin)
    time.sleep(2)
    p_off(pin)
    print(f"{pin} has squirted")
