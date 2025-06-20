'''

Given an array of integers nums, return the length of the longest consecutive 
sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 
greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

'''

nums = [2,20,4,10,3,4,5]



def longestConsecutive(nums):
    f_count = 0

    nums = list(set(nums))

    for i in range(len(nums)):
        count = 0
        position_a = nums[i]
        position_b = nums[i - 1]

        if position_a + 1 == position_b:
            count += 1
        else:
            f_count = count
            count = 0

    return f_count


print(longestConsecutive(nums))