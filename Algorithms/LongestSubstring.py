def lenghtLongestSubstring(s):
    aPointer = bPointer = maxSubString = 0
    listChar = []
    while(bPointer < len(s)):
        if s[bPointer] not in listChar:
            listChar.append(s[bPointer])
            bPointer += 1
            maxSubString = max(maxSubString, len(listChar))
        else:
            listChar.remove(s[aPointer])
            aPointer += 1
    return maxSubString

if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(lenghtLongestSubstring(s1))
    print(lenghtLongestSubstring(s2))
    print(lenghtLongestSubstring(s3))
