from typing import List


class Solution:

    def __init__(self):
        pass

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        O(n^2)
        """
        result_list = []
        a_index = 0
        for number_list_a in nums:
            b_index = 0
            new_nums = nums[a_index + 1:]
            for number_list_b in new_nums:
                if number_list_a + number_list_b == target:
                    result_list.append(a_index)
                    result_list.append(b_index + a_index + 1)
                    return result_list
                b_index += 1
            a_index += 1

    def two_sum_nums_hash(self, nums: List[int], target: int) -> List[int]:
        """
        O(n)
        """
        result_list = []
        hash_map = {}
        index = 0
        for num in nums:
            hash_map[num] = index
            index += 1

        for index in range(len(nums)):
            complement = target - nums[index]
            # It should contain other keys besides itself.
            is_not_current_position = hash_map[complement] != index
            if complement in hash_map.keys() and is_not_current_position:
                result_list.append(index)
                result_list.append(hash_map[complement])
                return result_list


if __name__ == '__main__':
    solution = Solution()
    # nums, target = [2, 7, 11, 15], 9
    # nums, target = [3, 3], 6
    nums, target = [3, 2, 4], 6
    result = solution.two_sum_nums_hash(nums, target)
    print(result)
