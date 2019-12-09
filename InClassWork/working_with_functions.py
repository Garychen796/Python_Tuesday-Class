def print_hello_world():
    print("Hello World")
    print("How are you")


print_hello_world()


def print_persons_name(first_name, last_name):
    print(first_name + "__________" + last_name)

print_persons_name('Preston', 'Hulcy')



def min(list_of_numbers):

    list_of_numbers.sort()
    #print(list_of_numbers[0])
    return list_of_numbers[0]

numbers = [10, 2, 100, 40, 37]

smallest_numbers = min(numbers)

print("Smallest Number:" + str(smallest_numbers))


