from math import pi

def area_circle(radius):
    area = pi * radius
    return area

radius = float(input("Enter the radius of circle: "))
temp = area_circle(radius)
print(temp)
 