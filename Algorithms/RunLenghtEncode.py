# aaabbcc
# aabbbcca
# abcd

def encoder(inputStr):

    charList = list(inputStr)

    previous = 0
    sb = ""
    counter = 1

    for i in range(len(charList)):
        if charList[i] == charList[i+1]:
            counter += 1
        elif charList[i] == charList[i+1]:
            sb + charList[i-1] + counter
            counter = 1
    return sb

    # print(len(charList))
    # if (charList == None or len(charList) == 0):
    #     return ""

    # counter = 1
    # sb = ""

    # for i in rangecharList):
    #     return i
    #     if charList[i] == charList[i + 1]:
    #         counter += 1
    #     elif charList[i] != charList[i + 1]:
    #         sb + charList[i] + counter
    #         counter = 1
    # return sb

lista = "aaabbcc"

print(encoder(lista))

# |a |a a b b c c
# counter = 2
# a |a |a b b c c
# counter = 3
# a a |a |b b c c
# charTuple[] = (counter, charList[i]) then counter = 0
# a a a |b |b c c
# counter = 2
# a a a b |b |c c
# charTuple
#
