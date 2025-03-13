import lgpio
import time

# Open a GPIO chip (usually /dev/gpiochip0)
chip = lgpio.gpiochip_open(0)

def p_on(pin):
    lgpio.gpio_claim_output(chip, pin)
    lgpio.gpio_write(chip, pin, 1)
    print(f"Relay on pin {pin} is now ON")

def p_off(pin):
    lgpio.gpio_claim_output(chip, pin)
    lgpio.gpio_write(chip, pin, 0)
    print(f"Relay on pin {pin} is now OFF")

def squirt(pin):
    p_on(pin)
    time.sleep(2)
    p_off(pin)
    print(f"{pin} has squirted")
