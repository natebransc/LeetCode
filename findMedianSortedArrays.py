# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1
        for i in nums2:
            combined.append(i)
        combined.sort()
        length = len(combined)
        if length % 2 != 0 and length != 2:
            return combined[int(length / 2)]
        else:
            return ((combined[int((length / 2) - 1)] + combined[int((length / 2))]) / 2)

test = Solution()
print(test.findMedianSortedArrays([],[1,2,3,4,5]))