def findFirstOcc():
    haystack, needle = 'hello', 'll'

    haystacklist = list(haystack)

    for i in range(len(haystack) - len(needle) + 1):
        if haystacklist[i] == needle[0]:
            if haystack[i:i + len(needle)] == needle:
                return i
            
        else : pass
        
    return -1


print(findFirstOcc())