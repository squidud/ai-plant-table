import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Function to turn on the relay (activate)
def p_on(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)  
    print(f"Relay on pin {pin} is now ON")

# Function to turn off the relay (deactivate)
def p_off(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  
    print(f"Relay on pin {pin} is now OFF")

# Function for ejecting a bit of water from the pump
def squirt(pin):
    p_on(pin)
    time.sleep(2)
    p_off(pin)
    print(f"{pin} has squirted")
