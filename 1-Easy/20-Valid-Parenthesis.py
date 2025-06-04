'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

'''

s = '[()]{}'

def is_valid(s):
    pass

    freq = {}
    splitstr = list(s)

    opening = ["(","[","{"]
    closing = [")","]","}"]

    if len(splitstr) % 2 != 0:
        return False
    
    for i in range(len(splitstr)):
        
        if splitstr[i] not in freq and splitstr[i] in opening:
            freq[splitstr[i]] = 1

        elif splitstr[i] in freq:
            freq[splitstr[i]] += 1

        if splitstr[i] in closing:
            if splitstr[i] == ")":
                freq[opening[0]] -= 1

            if splitstr[i] == "]":
                freq[opening[1]] -= 1

            if splitstr[i] == "}":
                freq[opening[2]] -= 1

    return all(value == 0 for value in freq.values()), freq

    



print(is_valid(s))
