'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''

s, t = 'anagram', 'margana'

# def isValidAnag(s, t):
#     if len(s) != len(t): return False
    
#     for i in range(1,len(s)):
#         if s[i] == t[len(t)-i-1]: continue
#         else : return False
#     return True

# print(isValidAnag(s,t))

def isValidAnag(s,t):
    s_freq = {}
    t_freq = {}
    freq = {}

    if len(s) != len(t):
        return False
    
    # for i in range(len(s)):
    #     if s[i] in s_freq:
    #         s_freq[s[i]] += 1

    #     else :
    #         s_freq[s[i]] = 1

    # for i in range(len(t)):
    #     if t[i] in t_freq:
    #         t_freq[t[i]] += 1

    #     else :
    #         t_freq[t[i]] = 1

    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] = 1
        else: freq[s[i]] += 1

    for i in range(len(t)):
        if t[i] in freq:
            freq[t[i]] -= 1

    return set(freq.values())

print(isValidAnag(s,t))


