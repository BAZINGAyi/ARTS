# Question: Flip String to Monotone Increasing
# A string of '0's and '1's is monotone increasing if it consists of
# some number of '0's (possibly 0), followed by some number of '1's
#  (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or
#  a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        Time O(n^2)
        Space O(1)
        :type S: str
        :rtype: int
        """

        if S is None or len(S) == 0:
            return 1

        length = len(S)
        min_counts = 2 ** 31 - 1
        for i in range(0, length + 1):
            left = '0' * i
            right = '1' * (length - i)
            comparaed_string = left + right
            # print(comparaed_string)

            flip_counts = 0
            for tuple in zip(S, comparaed_string):
                if tuple[0] != tuple[1]:
                    flip_counts += 1
            if flip_counts < min_counts:
                min_counts = flip_counts

        return min_counts

    def dp_prefix_suffix(self, S):
        # 使用两个数组，left 和 right. 位置 i 表示 left 和 right 分开的位置。
        # 现在也就是求，在将 left[0] 到 left[i] 中的元素变成 0 需要的次数。
        # 和 right[i] 到 right[n-1] 中的元素变成 1 需要的次数。
        # 之后求 left[i] 和 right[i] 加起来后的最小值就是，需要反转的次数。
        # DP 实现

        s_length = len(S)
        left_array = []
        right_array = [0] * s_length

        for i in range(0, s_length):
            node = left_array[i-1] + int(S[i]) - 0 if i > 0 else int(S[i]) - 0
            left_array.append(node)

        for i in reversed(range(0, s_length)):
            node = (1 - int(S[i]) + right_array[i+1]
                    if i < s_length - 1 else 1 - int(S[i]))
            right_array[i] = node

        min_counts = 2 ** 31 - 1
        for i in range(0, s_length):
            if i == s_length - 1:
                temp = min(left_array[i], right_array[i] + left_array[i-1])

            elif i == 0:
                temp = min(right_array[0], left_array[i] + right_array[i+1])

            else:
                temp = left_array[i] + right_array[i+1]

            min_counts = min(min_counts, temp)

        return min_counts


if __name__ == '__main__':

    solution = Solution()
    # print(solution.minFlipsMonoIncr('00110'))
    # print(solution.minFlipsMonoIncr('010110'))
    # print(solution.minFlipsMonoIncr('00011000'))
    # print(solution.minFlipsMonoIncr('11011'))
    print(solution.minFlipsMonoIncr('01110'))
    print(solution.dp_prefix_suffix('01110'))