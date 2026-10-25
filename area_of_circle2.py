from math import pi

def area_circle(r):
    result= pi * r* r
    return result
r = float(input("Enter the radius of circle: "))
temp  = area_circle(r)
print(temp)
