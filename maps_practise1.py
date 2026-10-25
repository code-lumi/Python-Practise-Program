import collections

dict1 = {"one": 1, "two":2, "three": 3}
dict2 = {"four ":4, "one": 1, "five": 5}

res = collections.ChainMap(dict1,dict2)
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()