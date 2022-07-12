# CORRECT 100%
# Runtime: 6392 ms, faster than 5.08% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.5 MB, less than 44.51% of Python3 online submissions for First Unique Character in a String.

"""
DESCRIPTION:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Constraints: 1 <= s.length <= 105 & s consists of only lowercase English letters.


TEST CASES:
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index,char in enumerate(s):
            if s.count(char) == 1:
                return index
        return -1
                