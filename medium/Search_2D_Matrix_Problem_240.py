"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        row_i = 0
        col_i = len(matrix[0]) - 1

        while row_i < len(matrix) and col_i >= 0:

            value = matrix[row_i][col_i]
            if value == target:
                return True
            if target < value:
                col_i -= 1
            if target > value:
                row_i += 1
        return False

    def searchMatrix_naive(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_i = len(matrix)
        col_i = len(matrix[0])
        for i in range(row_i):
            for j in range(col_i):
                if matrix[i][j] == target:
                    return True
        return False


Sol =Solution()

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target=100

print(Sol.searchMatrix(matrix,100))#False

print(Sol.searchMatrix(matrix,24))#True