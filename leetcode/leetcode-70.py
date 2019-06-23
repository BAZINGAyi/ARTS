# Question:
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# Example1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


# Example2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps

class Solution(object):
    def climbStairs_recursion(self, n):
        """
        :type n: int
        :rtype: int
        Time: O(2^n)
        Space: O(n)
        """
        if n <= 1:
            return 1
        else:
            return (self.climbStairs_recursion(n-1) +
                    self.climbStairs_recursion(n-2))

    def climbStairs_recursion_memorize(self, n, mem):
        """
        :type n: int
        :rtype: int
        Time: O(n)
        Space: O(n)
        """
        if n <= 1:
            mem[n] = 1

        if n not in mem:
            mem[n] = (self.climbStairs_recursion_memorize(n-1, mem) +
                      self.climbStairs_recursion_memorize(n-2, mem))
        return mem[n]

    def climbStairs_dp(self, n):
        """
        :type n: int
        :rtype: int
        Time: O(n)
        Space: O(1)
        """
        dp = {0: 1, 1: 1}
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs_fibonacci_number(self, n):
        """
        :type n: int
        :rtype: int
        Time: O(n)
        Space: O(1)
        """
        first, second, third = 1, 1, 0
        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return third


solution = Solution()
n = 7
# recursion
print(solution.climbStairs_recursion(n))
# memorize_recursion
mem = {}
print(solution.climbStairs_recursion_memorize(n, mem))
# Dp
print(solution.climbStairs_dp(n))
# fibonacci number
print(solution.climbStairs_fibonacci_number(n))