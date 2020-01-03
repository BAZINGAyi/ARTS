# Question: Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']'
# , determine if the input string is valid.
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.
# Example:
# Input: "()"
# Output: true
#
# Input: "()[]{}"
# Output: true
#
# Input: "(]"
# Output: false
#
# Input: "([)]"
# Output: false
#
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_list = {'(': ')', '{': '}', '[': ']'}
        stack = []

        if str == '':
            return True

        for char in s:
            if char in bracket_list.keys():
                stack.append(bracket_list[char])

            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
    print(s.isValid('()[]{}'))
    print(s.isValid('(]'))
    print(s.isValid('([)]'))
    print(s.isValid('{[]}'))
    print(s.isValid(']]]'))
