"""numbers = (1,2,3,4,5,6,7,8,9)

count_odd=0
count_even=0

for x in numbers:
    if not x% 2:
        count_even += 1
    else:
        count_odd +=1    

print("number of even numbers: ", count_even)        
print("number of odd numbers: ", count_odd)"""


count_even = 0
count_odd = 0

for i in range(1,100):
    if not i%2:
        count_even += 1
    else:
        count_odd += 1

print("number of even number are: ", count_even)
print("number of odd number: ", count_odd)