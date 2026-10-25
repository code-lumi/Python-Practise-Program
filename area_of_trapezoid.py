#Print the area of trapezoid

def area_trapezoid(base1, base2,height):
    area = (base1 + base2) * height
    return area

base1 = float(input("Enter the base1 of trapezoid: "))
base2 = float(input("Enter the base2 of trapezoid: "))
height = float(input("Enter the height of trapezoid: "))

temp =area_trapezoid(base1,base2,height)
print(temp)
