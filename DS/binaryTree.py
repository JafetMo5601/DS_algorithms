def SumUniqueInt(targetNumber):

    result = []

    # if the target number is even the loop
    # search for same values positives and
    # negatives to sum 0
    # if the target number is odd will happend the same
    # with the difference that the algorithm will add an 0
    # to return the lenght odd specified.

    if targetNumber % 2 == 0:
        for i in range(1, (targetNumber//2)+1):
            result.append(i)
            result.append(-i)
    else:
        result.append(0)
        for i in range(1, (targetNumber//2)+1):
            result.append(i)
            result.append(-i)

    return result

if __name__ == '__main__':
    print(SumUniqueInt(1))
