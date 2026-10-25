from math import *


#Addition using function
def additionR(num1, num2):
    result = num1 + num2
    return result

#Substraction using function
def substractionR(num1, num2):
    result = num1 - num2
    return result   

#multiplication using function
def multR(num1, num2):
    result = num1 * num2
    return result

#divison using function
def divisionR(num1,num2):
    result = num1/num2
    return result

#remainder using function
def remainderR(num1,num2):
    result = num1%num2
    return result

#this is floor division function
def floorR(num1,num2):
    result = num1//num2
    return result

#this is exponentation function
def exponentationR(num1,num2):
    result = num1**num2
    return result

#this is square root function
def squareR(num1,num2):
    result = sqrt(num1), sqrt(num2)
    return result

a = int(input("Enter the value of num1: "))
b = int(input("Enter the value of num2: "))

#calling square root function
sqr_sol = squareR(a,b)
print(sqr_sol)

'''
#calling floor division
flr_result = floorR(a,b)
print(flr_result)

exp_result = exponentationR(a,b)
print(flr_result)


#calling remainder function
rem_result = remainderR(a,b)
print(rem_result)


#calling division function
div_result = divisionR(a,b)
print(div_result)

#calling multiplication function
mult_result = multR(a,b)
print(mult_result)

#calling substraction function
sub_result = substractionR(a,b)
print(sub_result)

#calling addition function
add_result = additionR(a,b)
print(add_result)
'''