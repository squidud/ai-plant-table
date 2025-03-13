#for calibration uses only

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Define the analog input channel (A0)
chan = AnalogIn(ads, ADS.P0)

while True:
    print(f"Raw ADC Value: {chan.value}")
    time.sleep(1)
