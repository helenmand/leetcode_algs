# Correct 100%
# Runtime: 49 ms, faster than 55.21% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.8 MB, less than 55.26% of Python3 online submissions for Excel Sheet Column Number.

"""
DESCRIPTION:
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


TEST CASES:
Input: columnTitle = "A"
Output: 1

Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701

Input: columnTitle = "YZ"
Output: 676
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0
        multiplier = 1
        
        # last char : ord(char)
        # char before last char : ord(char) * 26 
        # - because this character is after Z, we multiply char's 
        # - ord with 26, ex. if it was B, orb(B) = 2 * 26
        # char before char before last char : ord(char)* 26 * 26
        # - this is because we are now counting after ZZ which is 702
        for char in reversed(columnTitle):
            ans += (ord(char) - 64) * multiplier
            multiplier *= 26
            
        return ans