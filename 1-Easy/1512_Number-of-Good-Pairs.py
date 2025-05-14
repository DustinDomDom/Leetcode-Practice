''''

Hint
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

'''


def numIdentical(nums):
    hashset = {}
    count = 0
    count_list = []

    for i in nums:
        if i in hashset:
            hashset[i] += 1
        else:
            hashset[i] = 1

    return hashset, count, count_list

nums = [1,2,3,1,1,3]

print(numIdentical(nums))