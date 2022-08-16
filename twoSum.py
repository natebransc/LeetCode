# LeetCode Practice Problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        size = len(nums)
        while i < size:
            try:
                j = nums.index(target - nums[i])
                if i != j:
                    return [i, j]
                else:
                    i += 1
            except:
                i += 1