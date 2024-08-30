import math

def circle_cal(radius):
    area = math.pi*(radius **2)
    circum =  2* math.pi * radius

    return area , circum

a,c = circle_cal(3)
print(a,c)

