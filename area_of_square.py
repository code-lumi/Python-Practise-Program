def area_square(side):
    area = side*side 
    return area

side = float(input("Enter the side of square: "))

temp = area_square(side) 
print(temp)