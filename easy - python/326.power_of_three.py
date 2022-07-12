# CORRECT 100%
# Runtime: 72 ms, faster than 84.05% of Python3 online submissions for Power of Three.
# Memory Usage: 14.4 MB, less than 15.30% of Python3 online submissions for Power of Three.

"""
DESCRIPTION:
Given an integer n, return true if it is a power of three. 
Otherwise, return false.
An integer n is a power of three, 
if there exists an integer x such that n == 3^x.

TEST CASES:
Input: n = 27
Output: true

Input: n = 0
Output: false

Input: n = 9
Output: true

Input: n = 45
Output: false

"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        
        while (num <= n):
            if num == n:
                return True
            else:
                num*=3
        return False