import math
angle=0
while angle<=120:
    deg=angle*(math.pi/180)
    sin_val=(math.sin(deg))
    cos_value=(math.cos(deg))
    print("sin of angle", (round(sin_val,4)))
    print("cosine of angle", (round(cos_value,4)))
    angle=angle+15