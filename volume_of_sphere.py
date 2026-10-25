#Write a Python program to get the volume of a sphere with radius six.

from math import pi

def volume_sphere(r):
    volume = 4/3*pi*r**3
    return volume

radius = float(input("Enter the radius of sphere: "))

result = volume_sphere(radius)
print("The volume of sphere is: ",result)