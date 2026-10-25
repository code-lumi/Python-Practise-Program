list1 = ['physics', 'chemistry', 2000, 1929]
list2 =[1,2,3,4,5,6,7]


'''
#deleting an element from list
print("List before deleting element")
print(list2)
del list2[6]
print("list after deleting element")
print(list2)

#updating an element from list
print("The value available at index 3 before updation")
print(list1[3])
list1[3] = 2023
print("The value availabe at index 3 after updation")
print(list1[3])

#searching an element from list
print("list1[1]: ", list1[1])
print("list2[1:5]", list2[1:5])

#creating a temporary list from parent list
tempList= list2[2:6]
print(tempList)
print(type(list1))
'''

a = len([1,2,3])
print(a)

b = [1,2,3]+[4,5,6]
print(b)

c = ("Hi!")*5
print(c)

d= 3 in [1,2,3,4]
print(d)

for x in [1,2,3]:
    print(x)
