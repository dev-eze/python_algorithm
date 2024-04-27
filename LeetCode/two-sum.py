'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''
from typing import List


nums = [3,2,3]
target = 6
def twoSum(nums, target):
    diff_dict = {}
    result = []

    for index, value in enumerate(nums): # 0 , 2
        diff = target - value  # 7 = 9 - 2
        diff_dict[diff] = index # list[7] = index0

        if index != nums.index(diff) and diff in nums: # 자기 자신은 안됌!
            result = (index, nums.index(diff))
            break

    return sorted(result) # index에 없는 경우 오류 반환


def twoSum2(nums, target):
    diff_dict = {}
    result = []

    for index, value in enumerate(nums): # 0 , 2
        diff = target - value  # 7 = 9 - 2

        if diff in diff_dict:
            result = [diff_dict[diff], index]
            break

        diff_dict[value] = index

    return sorted(result)




print(twoSum2(nums, target))
