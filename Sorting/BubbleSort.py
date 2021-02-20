class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.max = len(self.array)

    def sorting(self):

        for i in range(self.max - 1):
            swapped = False
            for j in range(self.max - 1 - i):
                if (self.array[j] > self.array[j + 1]):
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp
                    swapped = True

        return self.array

arr = [2,1,4,5]

test = BubbleSort(arr)

print(test.sorting())
