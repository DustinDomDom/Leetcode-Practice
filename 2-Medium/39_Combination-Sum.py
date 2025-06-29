'''

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to 
target is less than 150 combinations for the given input.

'''

import math 

candidates = [2,3,6,7]
target = 7

emp_arr = []

def check_combi(candidates, target):

    return math.comb(7, target)

print(check_combi(candidates, target))

