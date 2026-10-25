'''
num = int(input("Enter the number you waht to generate the table: "))

for i in range(1,11):
    result = num * i

    print(f"{num} X {i} = ", result)    
'''

values = input("Enter the comma seprated values: ")

list = values.split(",")
tuple = tuple(list)

print("List: ", list)
print("Tuple: ", tuple)