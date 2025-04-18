strs = ["flower","flow","flight"]


def longestCommonPrefix(arr):
    count = ""

    maxstr = len(min(arr, key=len))

    for i in range(maxstr):
        if arr[0][i] == arr[1][i] == arr[2][i]:
            count += arr[0][i]

        else:
            return count
    return count

print(longestCommonPrefix(strs))