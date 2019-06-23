# Question: A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


class Solution(object):
    def uniquePaths(self, row_number, column_number):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = [[None for i in range(column_number)] for j in range(row_number)]
        return self.recursion_paths_memorize(row_number - 1,
                                             column_number - 1,
                                             mem)

    def recursion_paths(self, x, y):
        """
        :param x: the row position of target
        :param y: the column position of target
        :return: How many possible unique paths are there?
        """
        if x == 0 or y == 0:
            return 1

        return (self.recursion_paths(x - 1, y) +
                self.recursion_paths(x, y - 1))

    def recursion_paths_memorize(self, row_x, column_y, mem):

        if row_x == 0 or column_y == 0:
            mem[row_x][column_y] = 1

        if mem[row_x][column_y] is None:
            mem[row_x][column_y] = (
                    self.recursion_paths_memorize(row_x - 1, column_y, mem) +
                    self.recursion_paths_memorize(row_x, column_y - 1, mem))

        return mem[row_x][column_y]

    def dp_paths(self, row_number, column_number):
        """
        According to the rule of discovery, it can be filled from top to bottom
        and from left to right.
        :param x: the row position of target
        :param y: the column position of target
        :return: How many possible unique paths are there?
        """
        mem = [[None for i in range(column_number)] for j in range(row_number)]
        for x in range(0, row_number):
            for y in range(0, column_number):
                if x == 0 or y == 0:
                    mem[x][y] = 1
                    continue
                mem[x][y] = mem[x-1][y] + mem[x][y-1]

        return mem[row_number-1][column_number-1]


solution = Solution()
row = 6
column = 6

print(solution.recursion_paths(row - 1, column -1))

print(solution.uniquePaths(row, column))

print(solution.dp_paths(row, column))