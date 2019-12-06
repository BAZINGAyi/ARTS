# 224. Basic Calculator
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces

# Example 1:
#
# Input: "1 + 1"
# Output: 2

# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3

# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand, n = 0, 1

        # Reverse string
        for index in range(len(s)-1, -1, -1):
            char = s[index]

            if char == " ":
                continue

            if char.isdigit():
                # transform number string to number
                # like "123" to 3+20+100=123
                operand = operand + int(char) * n
                n = n * 10
            else:
                # put before formatted string to the stack
                if n != 1:
                    stack.append(operand)
                    n, operand = 1, 0

                # due to the reversed order, '(' represents the end
                if char == '(':
                    self.eval(stack)
                # put current char to the stack like '+', '+', '-'
                else:
                    stack.append(char)

        if n != 1:
            stack.append(operand)

        return self.eval(stack)

    def eval(self, stack):
        result = stack.pop()
        while stack:
            sign = stack.pop()
            if sign == "+":
                operand = stack.pop()
                result = result + operand
            elif sign == "-":
                operand = stack.pop()
                result = result - operand
            elif sign == ")":
                break
        stack.append(result)
        return result


# 227. Basic Calculator II
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces . The integer division should truncate toward zero.
# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution1:
    def calculate(self, s):

        index = 0
        stack = []
        operand = 0
        pre_sign = "+"
        while index < len(s):
            char = s[index]
            if char == "":
                continue

            if char.isdigit():
                operand = 10 * operand + int(char)

            if char in ['+', '-', '*', '/'] or index == len(s)-1:
                if pre_sign == '+':
                    stack.append(operand)
                elif pre_sign == "-":
                    stack.append(-operand)
                elif pre_sign == "*":
                    stack.append(stack.pop() * operand)
                elif pre_sign == "/":
                    stack.append(int(stack.pop() / operand))

                pre_sign = char
                operand = 0

            index += 1

        return sum(stack)

# Leetcode 772 - Basic Calculator III
# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
# The expression string contains only non-negative integers, +, -, *, /
# operators , open ( and closing parentheses ) and empty spaces . The integer
# division should truncate toward zero.

# You may assume that the given expression is always valid.
# All intermediate results will be in the range of [-2147483648, 2147483647].

# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12


class Solution2:
    def calculate(self, s):

        index = 0
        stack = []
        operand = 0
        pre_sign = "+"
        while index < len(s):
            char = s[index]
            if char == "":
                continue

            if char.isdigit():
                operand = 10 * operand + int(char)

            if char in ['+', '-', '*', '/', '(', ')'] or index == len(s)-1:
                if char == "(":
                    operand, lenth = self.calculate(s[index+1:])
                    index = index + lenth

                if pre_sign == '+':
                    stack.append(operand)
                elif pre_sign == "-":
                    stack.append(-operand)
                elif pre_sign == "*":
                    stack.append(stack.pop() * operand)
                elif pre_sign == "/":
                    stack.append(int(stack.pop() / operand))

                if char == ")":
                    return sum(stack), index+1

                pre_sign = char
                operand = 0

            index += 1

        return sum(stack)


if __name__ == '__main__':
    solution = Solution()
    #print(solution.calculate('(11+(1+2-3)+1)'))
    #print(solution.calculate('123-1'))

    solution1 = Solution1()
    #print(solution1.calculate("1337"))

    solution2 = Solution2()
    print(solution2.calculate('(2+6* 3+5- (3*14/7+2)*5)+3'))
