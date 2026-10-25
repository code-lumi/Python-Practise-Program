def max_two(x,y):
    if x<y:
        return x
    else:
        return y



def max_three(x,y,z):
    return max_two(z,max_two(x,y))


#temp = max_two(n1,n2)
#print(temp)
print(max_three(2,3,4))
print(max_three(99,77,55))
