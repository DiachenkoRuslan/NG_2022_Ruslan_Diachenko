number = int(input("Enter number: ")) # Enter number

numList = []
for i in range(number):             # Start itteration(i) in range by length number,  
    numList.append(number)          # add number to numMassive,
    number-=1                       # number - 1 -> delete added number.

for i in range(len(numList)):       # Start itteration(i) in range length numList,
    for num in numList:             #  Number in numList,
        print(num, end=" ")         #  output without "newline"
    print("")                       #  space between numbers
    del numList[0]                  #  delete FIRST element in numList
