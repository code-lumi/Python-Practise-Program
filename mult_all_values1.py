
def mult_sum(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total   

print(mult_sum((3,5,7,9,1)))