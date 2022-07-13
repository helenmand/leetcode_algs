# Runtime: 49 ms, faster than 61.40% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 60.10% of Python3 online submissions for Happy Number.

"""
DESCRIPTION:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.


TEST CASES:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Input: n = 2
Output: false
"""
# recursive solution
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 7:
            return False
        else:
            sqr = 0
            for num in str(n):
                sqr += int(num)**2
            return self.isHappy(sqr)