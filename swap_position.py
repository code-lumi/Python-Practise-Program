def swapPosition(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [23,65,19,90]
pos1,pos2 = 1,3

print("Before swapping")
print(List)
print("After swapping")
print(swapPosition(List, pos1-1, pos2-1))