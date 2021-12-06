# CORRECT 100%
# Runtime: 36 ms, faster than 97.24% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.7 MB, less than 63.82% of Python3 online submissions for Search a 2D Matrix.

"""
DESCRIPTION: Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.


TEST CASES:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Input: matrix = [[1],[3]], target = 3
Output: true
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        searching_row = matrix[0] # searching the row the element is supposed to be
        
        c = 0 # counter
        for row in matrix:
            if c == 2: # if the counter is bigger than 2 mean that the row has not changed
                break  # after 2 loops so it is not possible to change, so we end the loop
            if target >= row[0]:
                searching_row = row
                c = 0
            c += 1
        
        # binary search
        low = 0
        high = len(searching_row) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if searching_row[mid] < target:
                low = mid + 1

            elif searching_row[mid] > target:
                high = mid - 1
            else:
                return True
        return False
