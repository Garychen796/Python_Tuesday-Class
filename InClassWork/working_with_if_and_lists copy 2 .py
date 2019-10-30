age = 15
if age <= 2:
    print("Baby")
else:
    if age < 4:
        print("Todder")
    else:
        if age < 20:
            print("Teenager")
        else:
            if age <65:
                print("Adule")
            else:
                print("Elder")

if age < 0:
    print("Invalid age")
elif age < 2:
    print("Baby")
elif age < 4:
    print("Todder")
elif age < 20:
    print("Teenager")
elif age < 14:
    print("Kid")
elif age < 65:
    print("Adult")
else:
    print("Elder")


if age < 0:
    print("Invalid age")
elif age < 2:
    print("Baby")
elif age >= 2 and age < 4:
    print("Todder")
elif age >= 4 and age < 20:
    print("Teenager")
elif age >= 20 and age < 65:
    print("Adult")
else:
    print("Elder")