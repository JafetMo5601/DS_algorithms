class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def hashing(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def setItem(self, key, value):
        index = self.hashing(key)
        self.arr[index].append((key, value))


    def getItem(self, key):
        index = self.hashing(key)
        for tuples in self.arr[index]:
            if tuples[0] == key:
                return tuples[1]

    def removeItem(self, key):
        index = self.hashing(key)
        for tuples in self.arr[index]:
            if tuples[0] == key:
                self.arr[index].remove(tuples)
        return self.arr

ht = HashTable()

ht.setItem("Jafet", 125)
print(ht.arr)
ht.setItem("bac", 525)
print(ht.arr)
ht.setItem("bca", 5312)
print(ht.arr)
print(ht.getItem("bac"))
print(ht.removeItem("bca"))































