class InterpolationSearch:

    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.lowestPosition = 0
        self.highestPosition = len(self.array) - 1

    def search(self):

        while self.lowestPosition <= self.highestPosition:

            mid = self.lowestPosition + int(float(((self.highestPosition - self.lowestPosition)) / (self.array[self.highestPosition] - self.array[self.lowestPosition])) * (self.target - self.array[self.lowestPosition]))

            if self.array[mid] == self.target:
                return mid

            else:
                if self.array[mid] < self.target:
                    self.lowestPosition = mid + 1
                else:
                    self.highestPosition = mid - 1

    def print(self):

        print(self.array)
        print(self.target)
        print(self.lowestPosition)
        print(self.highestPosition)

array = [1,2,3,4,5,6]
target = 2

test = InterpolationSearch(array, target)
print(test.search())
