from clicky import p_off, p_on, squirt
from wetness import read_moisture
import datetime
import json

luxpin = 27  # pin for light relay
h20pin = 17  # pin for pump relay

moisture = 0
lighton = False
last_squirt_time = None  # Store the last execution time

print("hardware looping")

while True:
    with open('/home/irl/ai-plant-table/static/data.json', 'r') as file:
        data = json.load(file)

    recmoist = data['moisture']
    reclux = data['sunlight']

    moisture = read_moisture()
    ctime = datetime.datetime.now()

    # Ensure squirt() runs only once per 30-minute interval
    if (ctime.minute % 30) == 0:
        if last_squirt_time is None or (ctime - last_squirt_time).total_seconds() >= 600:
            if moisture < recmoist:
                squirt(h20pin)
                last_squirt_time = ctime  # Update the last execution time
            print(f"FYI, recmoist is {recmoist} and reclux is {reclux}")

    # Control the light based on sunlight data
    if (ctime.hour >= (12 - (reclux / 2))) and (ctime.hour < (12 + (reclux / 2))):
        if not lighton:
            lighton = True
            print("turning on light")
            p_on(luxpin)
    else:
        if lighton:
            lighton = False
            p_off(luxpin)
