inputList  = input("Enter elements of list: ").split(",")

for index in range(len(inputList)):                 # Start index with 0 to range length inputList,
    inputList[index] = inputList[index].strip()     # Remove spaces in start and end

noRepeatList = {""}

for i in range(len(inputList)):             # Start itterations(i) in length by lengthList,
    noRepeatList.add(str(inputList[i]))     # Add to noRepeatList element from inputList by index,

noRepeatList.discard("")                    # Delete "" from noRepeatList because without it element(or other 1 element),
                                            # Method .add() not work!
print(noRepeatList)
