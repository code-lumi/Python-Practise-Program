#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and
#a tuple of those numbers.

values = (input("Enter the comma seprated numbers: "))

#conversion method
list = values.split(",")

tuple = tuple(list)

#now printing the rest
print("List: ", list)
print("Tuple: ", tuple)
