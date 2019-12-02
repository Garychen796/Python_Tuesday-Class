
def difference1(list1): 
    #x-y = []
    length = len(list1) 
    list1.sort() 
    x = list1[length-1]
    y = list1[0]
    return x-y
