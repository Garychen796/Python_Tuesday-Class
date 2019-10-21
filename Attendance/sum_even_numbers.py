# Sum N number of even numbers and output the result. 
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))

#Bonus
myList = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
sum(num for num in myList if not num%2)
