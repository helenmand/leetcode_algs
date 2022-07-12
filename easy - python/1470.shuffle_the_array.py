# CORRECT 100%
# Runtime: 76 ms, faster than 64.33% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.3 MB, less than 12.57% of Python3 online submissions for Shuffle the Array.

"""
DESCRIPTION:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].


TEST CASES:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        
        for x in range(0, n):
            y = x + n
            res.append(nums[x])
            res.append(nums[y])
       
        return res