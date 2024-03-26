import copy
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
c = copy.deepcopy(a)
b[0][1] = 10 # changes position [0][1] in both b and a
c[1][1] = 12
print(a) # prints [[1, 10, 3], [4, 5, 6]]
print(b) # prints [[1, 10, 3], [4, 5, 6]]
print(c)