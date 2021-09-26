# CORRECT 100%
# Runtime: 230 ms, faster than 31.44% of Python3 online submissions for Reverse String.
# Memory Usage: 18.4 MB, less than 81.72% of Python3 online submissions for Reverse String.

"""
DESCRIPTION: Write a function that reverses a string. The input string is given as an array of characters s.

1 <= s.length <= 105
s[i] is a printable ascii character.
Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


TEST CASES:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        lens = len(s)
        # simultanious changing the i character
        # with the len - i character.
        for i in range(0, lens // 2):
            temp = s[i]
            s[i] = s[lens - i -1]
            s[lens - i -1] = temp