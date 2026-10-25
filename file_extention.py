#Write a Python program that accepts a filename from the user and prints the extension of the file.

file_name =input("Enter the file name: ")

f_extnt = file_name.split(".")

print(repr(f_extnt[-1]))