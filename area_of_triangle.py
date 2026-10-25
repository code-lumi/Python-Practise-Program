def area_triangle(base,height):
    area = 0.5*base*height
    return area

x = float(input("Enter the base of triangle: "))
y = float(input("Enter the height of triangle: "))

result = area_triangle(x,y)
print(result)
