# Given a string, find the length of the longest substring
# without repeating characters.

# example one
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring,
#              "pwke" is a subsequence and not a substring.


class Solution:

    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        Time Complexity: (n^2)
        """

        max_length = 0

        for index, alphabet1 in enumerate(s):
            hash_map = {}
            hash_map[alphabet1] = True
            for alphabet2 in s[index+1:]:
                if alphabet2 in hash_map:
                    break
                else:
                    hash_map[alphabet2] = 0

            if hash_map.__len__() > max_length:
                max_length = hash_map.__len__()

        return max_length


    def lengthOfLongestSubstring_optimize(self, s: str) -> int:
        """
        Time Complexity: (n)
        find repeating elements, delete all the elements before the repeating element
        """

        hash_map = {}
        max_length = 0
        sliding_window_left = 0
        sliding_window_right = 0

        while sliding_window_left < len(s) and sliding_window_right < len(s):
            if s[sliding_window_right] not in hash_map:
                hash_map[s[sliding_window_right]] = sliding_window_right
                sliding_window_right = sliding_window_right + 1
                max_length = max(
                    max_length, sliding_window_right - sliding_window_left)
            else:
                hash_map.pop(s[sliding_window_left])
                sliding_window_left += 1

        return max_length

    def lengthOfLongestSubstring_optimize_much(self, s: str) -> int:
        """
        Time Complexity: (n)
        Check the duplicate values using hashmap
        Use two Pointers to obtain the length of the substring
        """
        max_length = 0
        pointer = 0
        hash_map = {}

        for current_index, alphabet in enumerate(s):

            if alphabet in hash_map:
            # pointer: Jump directly to the subscript of the repeating element,
            # omitting the deletion of the previous element. eg: pww, pointer can arrive at s[2]
            # ignore s[0], s[1]

            # max: we may meet repeating element, lead to the current pointer lees than before pointer
            # eg: 'pwwkewp' the first 'p' always in hashmap, when we found the last 'p' is repeated, 
            # pointer will be 1, it wrong  result 
            pointer = max(hash_map[alphabet] + 1, pointer)
                pointer = max(hash_map[alphabet] + 1, pointer)

            max_length = max(max_length, current_index - pointer + 1)
            hash_map[alphabet] = current_index

        return max_length



s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'
s4 = 'pwwkewp'
s5 = 'abfgkcgepd'
solution = Solution()
# print(solution.lengthOfLongestSubstring(s1))

print(solution.lengthOfLongestSubstring_optimize(s5))

