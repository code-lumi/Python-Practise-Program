#Print the area of parallelogram

def area_parallelogram(base,height):
    area = base*height
    return area

base = float(input("Enter the base of parallelogram: "))
height = float(input("Enter the height of parallelogram: "))

temp = area_parallelogram(base,height)
print(temp)