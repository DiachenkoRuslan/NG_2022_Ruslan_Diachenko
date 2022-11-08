number = int(input("Enter number: "))

for rep in range(number):       # rep - repeater.
    for el in range(number):    # element
        print(number - el, " ", end="")
    print()
    number -= 1


