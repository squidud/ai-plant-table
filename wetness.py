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

# Define calibration values (adjust these based on testing)
DRY_VALUE = 17855  # Value when soil is completely dry
WET_VALUE = 7975  # Value when soil is fully wet/submerged

def read_moisture():
    """
    Reads the soil moisture level from the capacitive sensor via ADS1115.
    Returns an integer percentage (0-100%) where:
    - 0% = Completely dry soil
    - 100% = Fully wet soil
    """
    moisture_value = chan.value  # Get raw 16-bit ADC value

    # Convert to percentage
    moisture_percent = 100 - ((moisture_value - WET_VALUE) / (DRY_VALUE - WET_VALUE) * 100)
    moisture_percent = max(0, min(100, moisture_percent))  # Limit to 0-100%

    return int(moisture_percent)