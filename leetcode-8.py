# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary
#  until the first non-whitespace character is found. Then, starting from
#  this character, takes an optional initial plus or minus sign followed by
#  as many numerical digits as possible, and interprets them as a numerical
#  value.
#
# The string can contain additional characters after those that form the
#  integral number, which are ignored and have no effect on the behavior of
#  this function.
#
# If the first sequence of non-whitespace characters in str is not a valid
#  integral number, or if no such sequence exists because either str is empty
#  or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
#  within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
#  value is out of the range of representable values,
#  INT_MAX (231 − 1) or INT_MIN (−231) is returned.


class Solution(object):
    def myAtoi(self, input_str: str):
        """
        :type str: input_str
        :rtype: int
        """

        input_str = input_str.strip(' ')
        if input_str == '':
            return 0
        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = - 2 ** 31

        subtract = False
        if input_str[0] == '-':
            input_str = input_str[1:]
            subtract = True
        elif input_str[0] == '+':
            input_str = input_str[1:]

        result = 0
        for char in input_str:
            if '0' <= char <= '9':
                result = result * 10 + int(char)
            else:
                break

        if subtract:
            return -result if -result > MIN_VALUE else MIN_VALUE
        else:
            return result if result < MAX_VALUE else MAX_VALUE


solution = Solution()
print(solution.myAtoi('+00000000012303'))