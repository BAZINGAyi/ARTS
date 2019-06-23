# Question: Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

# Notice:
# In 32-bit signed integer, as we know, it can divided positive
# and negative Integer. The first byte in left-to-right order represents signed.
# as a positive Integer, the maxvalue is OX7FFFFFFF that equals 2^31 - 1.
# the 7 can be explained 0111. the 0 represents positive.

# as a negative Integer, the minvalue is OX80000000 that equals -2^31
# the 8 can be explained 1111.

# Example:
# Input: 123
# Output: 321

# Input: -123
# Output: -321

# Input: 120
# Output: 21


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        MAX_INT_VALUE = 2 ** 31 - 1
        MIN_INT_VALUE = - (2 ** 31)

        if x > 0:
            reverse_result = int(str(x)[::-1])
        else:
            reverse_result = -1 * int(str(0 - x)[::-1])

        if reverse_result > MAX_INT_VALUE or reverse_result < MIN_INT_VALUE:
            return 0

        return reverse_result

    def reverser_approach1(self, x):
        MAX_INT_VALUE = 2 ** 31 - 1
        MIN_INT_VALUE = - (2 ** 31)

        flag = False
        if x < 0:
            flag = True
            x = -x

        result = 0
        while x != 0:
            value = x % 10
            x = int(x/10)
            result = result * 10 + value

        if flag:
            result = -result

        if result > MAX_INT_VALUE or result < MIN_INT_VALUE:
            return 0
        else:
            return result


solution = Solution()
input_int = 689685421788888888888888
print(solution.reverser_approach1(input_int))

