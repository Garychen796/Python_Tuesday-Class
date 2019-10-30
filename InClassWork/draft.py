mylist = [ 1, 2, 3, -7]
print(mylist)
for i in range(len(mylist)):
    mylist[i] = -mylist[i]
print(mylist)