def LookPairNumbers(arr, target):
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] + arr[j] == target:
    #             return [arr[i], arr[j]]
    pointerA = 0
    pointerB = len(arr)-1
    arr.sort()
    while pointerB > pointerA:
        if arr[pointerA] + arr[pointerB] == target:
            return [arr[pointerA], arr[pointerB]]
        elif arr[pointerA] + arr[pointerB] < target:
            pointerA += 1
        else:
            pointerB -= 1

if __name__ == '__main__':
    arr1 = [1,2,4,8,9]
    arr2 = [4,8,3,1,2,3]
    print(LookPairNumbers(arr1, 5))
    print(LookPairNumbers(arr2, 5))
