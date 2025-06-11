'''

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

'''


nums = [1, 2, 3, 3]

def hasDup(nums):
    return len(nums) != len(set(nums))
