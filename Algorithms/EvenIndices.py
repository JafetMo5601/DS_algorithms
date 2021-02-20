def addEvenIndices(arr):
    newArr = []
    index = 0

    while index < len(arr):
        newArr.append(arr[index])
        index += 2

    return newArr

if __name__ == '__main__':
    arr = [9,4,3,1,2,7]
    print(addEvenIndices(arr))
