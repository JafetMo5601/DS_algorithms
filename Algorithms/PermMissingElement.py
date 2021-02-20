L, R = 0, 1

def findMissingNumber(arr):
    global L, R
    arr.sort()
    if len(arr) <= 1 or arr[L] != 1:
        return 1
    elif (arr[L]+1) != arr[R]:
        result = arr[L]+1
        return result
    elif (arr[L]+1) == arr[R]:
        L, R = L+1, R+1
        return findMissingNumber(arr)

if __name__ == '__main__':
    arr = [4,1,3,2,6]
    print(findMissingNumber(arr))
