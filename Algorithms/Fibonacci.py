def numberInFibPosition(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = numberInFibPosition(n-1) + numberInFibPosition(n-2)
    return result

print(numberInFibPosition(6))
