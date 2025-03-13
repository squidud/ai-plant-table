from clicky import p_off, p_on, squirt
from wetness import read_moisture
import datetime
import json

luxpin = 27 #pin for light relay

h20pin = 17 #pin for pump relay

ctime = datetime.datetime.now() #use ctime.hour, ctime.minute, ctime.second and so on

moisture = 0

lighton = False

while True:
    with open('/home/irl/ai-plant-table/static/data.json', 'r') as file:
        data = json.load(file)
    
    recmoist = data['moisture']

    reclux = data['sunlight']

    moisture = read_moisture()
    ctime = datetime.datetime.now()

    if (ctime.minute%10) == 0:
        if moisture < recmoist:
            squirt(h20pin)
        print("FYI, recmoist is "+str(recmoist)+" and reclux is "+str(reclux))

    if (ctime.hour >= (12-(reclux/2))) and (ctime.hour < (12+(reclux/2))):
        if lighton == False:
            lighton = True
            p_on(luxpin)
    else:
        if lighton == True:
            lighton = False
            p_off(luxpin)