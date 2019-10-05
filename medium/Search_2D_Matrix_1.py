"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


"""


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        #         base condition if matrix is empty

        if not matrix:
            return False
        #  row index
        row_i = 0
        # column index
        col_i = len(matrix[0]) - 1
        # print(matrix[0][0])
        while row_i < len(matrix) and col_i >= 0:
            if matrix[row_i][col_i] == target:
                return True
            else:
                if target < matrix[row_i][col_i]:
                    col_i -= 1
                if target > matrix[row_i][col_i]:
                    row_i += 1

        return False

Sol =Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print(Sol.searchMatrix(matrix,target)) # False

target=3
print(Sol.searchMatrix(matrix,target)) # true
