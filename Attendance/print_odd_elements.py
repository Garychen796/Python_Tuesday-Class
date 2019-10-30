list = [ 5, -3, 10, 24, 37, -128]
odd_P = []
count = 0
for X in list:
    if count % 2 == 1:
        odd_P.append(X)
    count += 1
print(odd_P)