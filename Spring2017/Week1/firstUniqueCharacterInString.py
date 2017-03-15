# Given a string, find the first non-repeating character in it and return
# it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0
#
# s = "loveleetcode"
# return 2
#
# Note: you may assume the string contains only lowercase letters

def firstUniqChar(s):
    counts = {char: s.count(char) for char in s}
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1

    # a more pythonic way to write this loop is to use
    # the built-in `enumerate` method to gain access to
    # the index and the element of the list simultaneously
    #
    #
    # this way is fine too, just not as a clean:


def countsDict(s):
    d = {}

    # a "pythonic" way to write this loop is to use
    # the lists' built-in `count` method:
    #
    # d = {char: s.count(char) for char in s}
    for char in s: 
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def tests():
    s1 = "leetcode" #0
    s2 = "loveleetcode" #2
    s3 = "apple" #0
    s4 = "" #-1
    s5 = "aabbcc" #-1
    s6 = "aabbc" #4
    print(firstUniqChar(s1) == 0)
    print(firstUniqChar(s2) == 2)
    print(firstUniqChar(s3) == 0)
    print(firstUniqChar(s4) == -1)
    print(firstUniqChar(s5) == -1)
    print(firstUniqChar(s6) == 4)

tests()