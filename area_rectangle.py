def area_of_rectangle(length,width):
    area = length* width
    return area

len = float(input("Enter the length of rectangle: "))
wid = float(input("Enter the width of rectangle: "))

result = area_of_rectangle(len,wid)
print(result)