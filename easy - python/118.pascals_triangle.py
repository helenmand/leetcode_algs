"""
DESCRIPTION:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

        [1]
      [1] [1]
    [1] [1] [1]
  [1] [3] [3] [1]
[1] [4] [6] [4] [1]

TEST CASES:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        
        for i in range(0, numRows):
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
        return answer

            




    