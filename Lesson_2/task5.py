inputList  = input("Enter elements of list: ").split(",")

numList = []
sumNumList = 0

for elem in inputList:
    numList.append(int(elem))
for elem in numList:
    sumNumList += elem


print("Smallest number in list: ", min(numList))
print("Biggest number in list: ", max(numList))
print("Sum all numbers in list: ", sumNumList)
