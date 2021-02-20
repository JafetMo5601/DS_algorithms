def ss(arr):
    for i in range(len(arr)):
        lowestIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowestIndex]:
                lowestIndex = j
        if lowestIndex != i:
            temp = arr[i]
            arr[i] = arr[lowestIndex]
            arr[lowestIndex] = temp
    return arr

if __name__ == '__main__':
    arr = [9,4,3,1,2,7]
    print(ss(arr))

