def shiftNumber(number, arr):
    arr.insert(0,number)

def Rotate(arr, k):
    if k == 0:
        return arr
    else:
        while k > 0:
            shiftNumber(arr[-1], arr)
            arr.pop(-1)
            k -= 1
        return arr

arr = [3,8,9,7,6]
print(Rotate(arr, 3))
