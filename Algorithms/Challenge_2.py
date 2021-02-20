class Challenge2:

    def byLinearSearch(self, listOfNumbers):

        multiplication = 1
        productList = []

        for i in range(1,len(listOfNumbers)+1):
            for j in range(i+1, len(listOfNumbers)+1):
                multiplication *= j
            productList.append(multiplication)
            multiplication = 1
        return productList

List = [1,2,3,4,5]

test_1 = Challenge2()
print(test_1.byLinearSearch(List))
