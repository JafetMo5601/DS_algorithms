def findOdds(arr):
    arr.sort()
    if len(arr) <= 1:
        return arr[1]
    for i in range (0, len(arr), 2):
        if i+1 == len(arr):
            return arr[i]
        if arr[i] != arr[i+1]:
            return arr[i]

print(findOdds([9, 3, 9, 3, 7, 9, 9]))
