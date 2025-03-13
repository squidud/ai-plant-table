from clicky import p_off, p_on, squirt
import time

rp1 = 17
rp2 = 27
print("Now testing...")

p_on(rp1)
time.sleep(5)
p_off (rp1)
time.sleep(5)

p_on(rp2)
time.sleep(5)
p_off (rp2)
time.sleep(5)

squirt(rp1)
time.sleep(5)
squirt(rp2)

print("Done testing!")