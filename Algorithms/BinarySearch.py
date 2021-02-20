class binarySearch():

    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.left = 0
        self.right = len(self.arr) - 1

    def search(self):

        self.arr.sort()

        while self.left <= self.right:
            mid = (self.arr[self.left] + self.arr[self.right]) // 2
            if self.arr[mid] == self.n:
                return mid
            elif self.n < self.arr[mid]:
                self.right = mid - 1
            else:
                self.left = mid + 1

        return -1

    def printAttributes(self):

        print(self.arr)
        print(self.n)
        print(self.left)
        print(self.right)

arr = [1,2,3,4]

x = binarySearch(arr, 2)
print(x.search())
