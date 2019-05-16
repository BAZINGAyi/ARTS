# Question:
# ZigZag Conversion

# Description:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
#  of rows like this: (you may want to display this pattern in a fixed font for
#  better legibility)

# Example:
# eg1: input: "PAYPALISHIRING" 3, output: "PAHNAPLSIIGYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R

# Notice:
# we can found the variation of the provided str is like:
# 'P' row[0] step = 1
# 'A' row[1] step = 1
# 'Y' row[2] step = -1
# 'P' row[1] step = -1
# 'A' row[0] step = 1
# 'L' row[1] step = 1
# 'I' row[1] step = -1
# 'H' row[0] step = -1
# .......

# So, wo can make a conclusion, when the row is 0, step will 1.
# the step will 2 when the row is numrows - 1.

# eg2: input: "PAYPALISHIRING" 3, output: "PINALSIGYAHRPI"
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution(object):

    def __init__(self):
        pass

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s

        zigzag = ['' for i in range(numRows)]

        row, step = 0, 1

        for character in s:
            if row == 0:
                step = 1

            elif row == numRows - 1:
                step = -1

            zigzag[row] += character
            row += step

        return ''.join(zigzag)


solution = Solution()
str_1 = "AB"
print(solution.convert(str_1, 1))

