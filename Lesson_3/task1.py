def inputNum(text):
    return int(input(text))

def inputOp():
    return input("Enter operation (+, -, *, /, ^, ~): ")

def addNums(num1, op, num2):
    return num1 + num2

def minusNums(num1, op, num2):
    return num1 - num2

def divNums(num1, op, num2):
    return num1 / num2

def multipleNums(num1, op, num2):
    return num1 * num2

def powerNums(num1, op, num2):
    return num1 ** num2

def squareNums(num1, op, num2):
    return num1 ** (1/num2)

def result(num1, op, num2):
    if op == "+":
        return addNums(num1, op, num2)
    if op == "-":
        return minusNums(num1, op, num2)
    if op == "*":
        return divNums(num1, op, num2)
    if op == "/":
        return multipleNums(num1, op, num2)
    if op == "^":
        return powerNums(num1, op, num2)
    if op == "~":
        return squareNums(num1, op, num2)

def main():
    num1 = inputNum("Enter num1: ")
    operation = inputOp()
    num2 = inputNum("Enter num2: ")
    resultNum = result(num1, operation, num2)
    print("Result: ", resultNum)

main()
