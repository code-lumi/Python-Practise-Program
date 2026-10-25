lst = [1,2,3,4,5,6,7]
i = 8
def list_check():
    if i in lst:
        print(i, "is present in list")
    else:
        print(i, "is not present in list")

lit = list_check()
print(lit) 