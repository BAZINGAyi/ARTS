# Question:
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

# Type: dichotomy

# You may assume nums1 and nums2 cannot be both empty.
# Notice：
# 1. Required time complexity is O(log (m+n))，so We need to use the dichotomy
# to search.

# 2. we need to understand the meaning of median. if length of array is odd,
# so the median is a[len(a)/2]

# if length of array is even, so the median is (a[len(a)/2 - 1] + a[len(a)/2])/2
# 3. we will two sorted array nums1 and nums2 is divided into two parts.
# nums1 was divided into nums1_left and nums1_right.
# nums2 was divided into nums2_left and nums2_right.
# then, guarantee the length of nums1_left add the length of nums2_left
# equal length of nums1_right add the length of nums2_right.
# so, we will found the median only have associated with the max(nums1_left)，
# max(nums2_left),  min(nums1_right)
# and min(nums1_right).


import sys
from typing import List


class Solution:

    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if nums1.__len__() > nums2.__len__():
            return self.findMedianSortedArrays(nums2, nums1)

        nums1_length = nums1.__len__()
        nums2_length = nums2.__len__()

        integer_max_value = sys.maxsize
        integer_min_value = -sys.maxsize - 1

        low = 0
        high = nums1_length

        while low <= high:

            partition_x_length = int((low + high)/2)
            partition_y_length = int((nums1_length + nums2_length + 1)/2) - partition_x_length

            # The length of the array number1 left part is 0, so add an unreachable value
            max_left_x_value = integer_min_value if partition_x_length == 0 else nums1[partition_x_length - 1]
            # The length of the array number1 left part equal the length of number1, so add an unreachable value
            min_right_x_value = integer_max_value if partition_x_length == nums1_length else nums1[partition_x_length]

            max_left_y_value = integer_min_value if partition_y_length == 0 else nums2[partition_y_length - 1]
            min_right_y_value = integer_max_value if partition_y_length == nums2_length else nums2[partition_y_length]

            if max_left_x_value <= min_right_y_value and max_left_y_value <= min_right_x_value:

                if (nums1_length + nums2_length) % 2 == 0:
                    return (min(min_right_x_value, min_right_y_value) + max(max_left_x_value, max_left_y_value))/2.0
                else:
                    return max(max_left_x_value, max_left_y_value)/1.0

            elif max_left_x_value > min_right_y_value:
                high = partition_x_length - 1

            else:
                low = partition_x_length + 1

        raise Exception('Arrays not sorted')


solution = Solution()

nums_1 = [1, 2, 3, 5, 6]
nums_2 = [4]

print(solution.findMedianSortedArrays(nums_1, nums_2))






