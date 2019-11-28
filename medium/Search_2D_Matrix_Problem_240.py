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



"""
Try this soluion and understand
https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/396054/What's-the-time-complexity-of-this-approach
"""

"""
class Solution:
    def tighten(self, Y1, Y2, X1, X2):
        if Y1 == Y2 and X1 == X2:
            return self.matrix[Y1][X1] == self.target

        t, b = Y1, Y2
        while t < b:
            i = (t+b+1) // 2
            if self.matrix[i][X1] < self.target:
                t = i
            elif self.matrix[i][X1] > self.target:
                b = i-1
            else:
                return True
        y2 = b

        t, b = Y1, Y2
        while t < b:
            i = (t+b) // 2
            if self.matrix[i][X2] < self.target:
                t = i+1
            elif self.matrix[i][X2] > self.target:
                b = i
            else:
                return True
        y1 = b

        l, r = X1, X2
        while l < r:
            i = (l+r+1) // 2
            if self.matrix[Y1][i] < self.target:
                l = i
            elif self.matrix[Y1][i] > self.target:
                r = i-1
            else:
                return True
        x2 = r

        l, r = X1, X2
        while l < r:
            i = (l+r) // 2
            if self.matrix[Y2][i] < self.target:
                l = i+1
            elif self.matrix[Y2][i] > self.target:
                r = i
            else:
                return True
        x1 = r

        return self.tighten(y1, y2, x1, x2)
    
    def searchMatrix(self, matrix, target):
        self.matrix = matrix
        self.target = target
        return self.tighten(0, len(matrix)-1, 0, len(matrix[0])-1) if matrix and matrix[0] else False

"""