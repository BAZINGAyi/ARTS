# Question: Daily Temperatures
# Given a list of daily temperatures T, return a list such that, for each day in
#  the input, tells you how many days you would have to wait until a warmer
#  temperature. If there is no future day for which this is possible, put 0
#  instead.

# Example1:
# T = [73, 74, 75, 71, 69, 72, 76, 73]
# [1, 1, 4, 2, 1, 1, 0, 0]

# Note:
# the length of temperatures will be in the range [1, 30000]
# Each temperature will be an integer in the range [30, 100]


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        stack_sky = [0] * len(T)
        for index, element in enumerate(T):
            if stack.__len__() > 0:
                tem = T[stack[-1]]
                while stack and element > tem:
                    stack_sky[stack[-1]] = index - stack[-1]
                    stack.pop()
                    if stack.__len__() > 0:
                        tem = T[stack[-1]]
            stack.append(index)

        return stack_sky


if __name__ == '__main__':
    example_list_1 = [73, 74, 75, 71, 69, 72, 76, 73]
    example_list_2 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    solution = Solution()
    print(solution.dailyTemperatures(example_list_2))


