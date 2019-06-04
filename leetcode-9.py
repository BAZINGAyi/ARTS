class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def isPalindrome_method2(self, x):

        if x % 10 == 0 and x != 0:
            return False

        reversed_value = 0
        while reversed_value < x:
            reversed_value = reversed_value * 10 + x % 10
            x /= 10
        # x == reversed_value is even number,
        # x == reversed_value/10 is odd number
        return x == reversed_value or x == reversed_value/10

