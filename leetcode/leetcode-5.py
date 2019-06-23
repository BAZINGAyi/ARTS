# Question:
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.

# Type: DP

# Notice:
# 1. str[i:j] includes the index i，but it not includes j.
# and str[i:i] will be ''

# 2. There are two situations in Palindrome.
# the first is the center of symmetrical_type, like 'aba'
# the second is the center of axisymmetric type, like 'abba'

# 3. we can traverse this str from 0 to len(str). and set str[i] is
# center(i is index of string) and try to judge whether the characters
# on both sides of i satisfy the rules of the palindrome.


class Solution:

    def __init__(self):
        pass

    def longestPalindrome(self, s: str) -> str:
        """
        Time complexity : O(n^2).
        Space complexity : O(1).
        """

        palindrome_str = ''
        for index in range(len(s)):
            # symmetrical_type
            the_str_of_the_center_of_symmetrical_type = (
                self.getlongestPalindrome(s, index, index))

            the_length_of_the_center_of_symmetrical_type = (
                len(the_str_of_the_center_of_symmetrical_type))

            if the_length_of_the_center_of_symmetrical_type > len(
                    palindrome_str):
                palindrome_str = the_str_of_the_center_of_symmetrical_type

            # axisymmetric type
            the_str_of_the_center_of_axisymmetric_type = (
                self.getlongestPalindrome(s, index, index + 1))

            the_length_of_the_center_of_axisymmetric_type = (
                len(the_str_of_the_center_of_axisymmetric_type))

            if the_length_of_the_center_of_axisymmetric_type > len(
                palindrome_str):
                palindrome_str = self.getlongestPalindrome(s, index, index + 1)

        return palindrome_str

    def getlongestPalindrome(self, s: str, left_index: int, right_index: int):

        while left_index >= 0 and right_index < len(s) and (
                s[left_index] == s[right_index]):
            left_index -= 1
            right_index += 1

        return s[left_index + 1:right_index]


solution = Solution()

str1 = 'babad'

str2 = 'cbbd'

print(solution.longestPalindrome(str1))

print(solution.longestPalindrome(str2))
