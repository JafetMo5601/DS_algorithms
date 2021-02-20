def isOdd(number):
    if (number&1 == 0):
        print('Es par')
    else:
        print('Es impar')

if __name__ == '__main__':
    isOdd(1)
    isOdd(2)
    isOdd(3)
    print(bin(2)[2:][-1])
