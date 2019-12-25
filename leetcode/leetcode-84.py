from typing import List
# Problem: 84. Largest Rectangle in Histogram

# Given n non-negative integers representing the histogram's bar height
#  where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10


class Solution:
    def largestRectangleArea_old(self, heights: List[int]) -> int:
        """
        O(n^2) -> 超时了，无法提交成功
        :param heights:
        :return:

         思路：最后形成最大的矩形面积，肯定是以给定的数组中某个位置连续矩形的最矮位置。
         从 index=0 的位置开始，假定它是这样的位置，然后向左向右开始扫描，找出其连续的矩形
         面积，然后依次比较这些找到的矩形面积。
        """
        max_area = 0
        index = 0
        list_length = len(heights)
        while index < list_length:
            area = heights[index]
            left_index = index - 1
            while left_index > -1:
                if heights[left_index] >= heights[index]:
                    area += heights[index]
                    left_index -= 1
                else:
                    break

            right_index = index + 1
            while right_index < list_length:
                if heights[right_index] >= heights[index]:
                    area += heights[index]
                    right_index += 1
                else:
                    break
            max_area = max_area if max_area > area else area
            index += 1

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # add 0 to query the last local peak area
        # if the last height is still the highest
        heights.append(0)
        # definite a stack to record the heights position
        # to get the local peak area
        heights_position = []
        max_area = 0
        index = 0
        while index < len(heights):
            if len(heights_position) == 0 or heights[heights_position[-1]] <= heights[index]:
                heights_position.append(index)
                index += 1
            else:
                popped_position = heights_position.pop()
                # get the continuous area of the smallest rectangle
                if len(heights_position) == 0:
                    max_area = max(max_area, index * heights[popped_position])
                # Get maximum area of rectangle in monotonically increasing
                else:
                    max_area = max(max_area,
                                   (index - 1 - heights_position[-1]) * heights[popped_position])
        return max_area


if __name__ == '__main__':
    soluction = Solution()
    print(soluction.largestRectangleArea_old([2, 1, 5, 6, 2, 3]))
    print(soluction.largestRectangleArea_old([2, 1, 2]))

    print(soluction.largestRectangleArea([1, 2, 3, 1, 2, 3]))
    print(soluction.largestRectangleArea([2, 1, 2]))
    print(soluction.largestRectangleArea([4,2,0,3,2,5]))
