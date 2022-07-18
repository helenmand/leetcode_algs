"""
DESCRIPTION:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

        [1]
      [1] [1]
    [1] [1] [1]
  [1] [3] [3] [1]
[1] [4] [6] [4] [1]

TEST CASES:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]

"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = []
        
        for i in range(0, rowIndex + 1):
            if i < 2:
                row = [1] * (i + 1)
                
            elif i == 2:
                row = [1] * (i + 1)
                row[1] = 2
                
            else:
                row = [1] * (i + 1)
                for j in range(1, i):
                    row[j] = (answer[i-1][j-1] + answer[i-1][j])
            answer.append(row)
        
        return answer[rowIndex]