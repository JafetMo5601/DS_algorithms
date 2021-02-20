def convertDecToBinary(number):
    binaryResult = bin(number)[2:]
    return binaryResult

def findGapsOnBinaries(targetNumber):
    targetNumber = convertDecToBinary(targetNumber)
    gapsCounter = 0
    gapsCounterList = []
    leftPointer, rightPointer = 0, len(targetNumber)-1

    while leftPointer <= rightPointer:
        valueLeftPointer, valueRightPointer = targetNumber[leftPointer], targetNumber[rightPointer]
        if int(valueLeftPointer) != 1:
            gapsCounter += 1
        else:
            gapsCounterList.append(gapsCounter)
            gapsCounter = 0
        leftPointer += 1
    return max(gapsCounterList)

# 1001
print(findGapsOnBinaries(9))
# 1 0100
print(findGapsOnBinaries(20))
# 10 0001 0001
print(findGapsOnBinaries(529))
