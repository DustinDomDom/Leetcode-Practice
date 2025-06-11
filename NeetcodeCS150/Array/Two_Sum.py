'''

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

'''

nums, target = [4,5,6], 10

def twosum(nums, target):
    if len(nums) == 2:
        return nums.index(nums[0]), nums.index(nums[1])
    
    prev_val = {}

    for index, val in enumerate(nums):
        diff = target - val
        if diff in prev_val:
            return [prev_val[diff], index], prev_val
        prev_val[val] = index




print(twosum(nums, target))