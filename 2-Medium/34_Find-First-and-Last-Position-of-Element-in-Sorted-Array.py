'''

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1: ----------------------------------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2: ----------------------------------
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3: ----------------------------------
Input: nums = [], target = 0
Output: [-1,-1]
 
'''

nums = [5,7,7,8,8,10]
target = 8

def startPos(nums, target):
    lo, hi = 0, len(nums) - 1
    start = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            start = mid
            hi = mid - 1  # keep looking to the left
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return start

def endPos(nums, target):
    lo, hi = 0, len(nums) - 1
    end = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            end = mid
            lo = mid + 1  # keep looking to the right
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return end

def searchRan():

    if len(nums) == 0: return [-1, -1]
    
    return [startPos(nums, target), endPos(nums, target)]
