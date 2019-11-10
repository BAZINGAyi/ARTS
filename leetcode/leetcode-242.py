# Question:
# Given two strings s and t , write a function to determine if t is an
# anagram of s.

# Type: string or array

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters?
# How would you adapt your solution to such case?
import string


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # get all lower alphabets
        lower_alphabets = string.ascii_lowercase

        # we can init a hash map to represent the count of alphabets.
        lower_alphabets_map = {alphabet: 0 for alphabet in lower_alphabets}

        # Traverse the string "s" and plus 1 to the count of alphabet
        # that appear
        for index in s:
            if index in lower_alphabets_map.keys():
                lower_alphabets_map[index] += 1

        # Then Traverse the string "t" and subtract 1 to the count of alphabet
        # that appear
        for index in t:
            if index in lower_alphabets_map.keys():
                lower_alphabets_map[index] -= 1

        # if the count of all alphabets in the hash map is 0, then the string
        # "s" and "t" are anagrams.
        is_anagram = False
        for value in lower_alphabets_map.values():
            if value != 0:
                return is_anagram
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('abc', 'abc'))
