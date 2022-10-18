
#Important notice!
print("NOTICE! ^ - a squared b.(Example: 2^3 = 8).")
print("NOTICE! ~ - root a on b. (Example: 16~2 = 4).")
# Enter first number 
firstNumber = int(input("Enter first number: "))

# Enter second number 
secondNumber = int(input("Enter second number: "))

# Enter operation(+, -, *, /) for firstNumber and secondNumber
operation = input("Enter operation( +, - , *, /, ^, ~ ): ")


# if operation +, output: a + b = c
if operation == '+':
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber + secondNumber))

# if operation -, output: a - b = c
elif operation == "-":
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber - secondNumber))

# if operation *, output: a * b = c
elif operation == "*":
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber * secondNumber))

# if operation /, output: a / b = c
elif operation == "/":
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber / secondNumber))

# if operation *, output: a ^ b = c
elif operation == "^":
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber ** secondNumber))

# if operation ~, output: a ~ b = c (root operation)
elif operation == "~":
    print("Result: " + str(firstNumber) + operation + str(secondNumber) + " = " + str(firstNumber ** (1/secondNumber)))

# if operation not equal +, -, *, /
else:
    print("I don't know [ " + operation + " ] operation!")
