'''

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

'''

s = "jar"
t = "jam"

def validAnagram(s,t):
    if len(s) != len(t):
        return False
    

    temp_dict1 = {}
    temp_dict2 = {}

    for i in range(len(s)):
        if s[i] not in temp_dict1:
            temp_dict1[s[i]] = 1

        else:
            temp_dict1[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in temp_dict2:
            temp_dict2[t[i]] = 1

        else:
            temp_dict2[t[i]] += 1

    return temp_dict1 == temp_dict2

print(validAnagram(s,t))