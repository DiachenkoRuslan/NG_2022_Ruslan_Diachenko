number = int(input("Enter number: "))

numList = []
for i in range(number):
    numList.append(number)
    number-=1

for i in range(len(numList)):
    for j in numList:
        print(j, end=" ")
    print("")
    del numList[0]
