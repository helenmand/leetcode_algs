"""
DESCRIPTION:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


TEST CASES:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for letter in max(strs):
            res += letter
            
            for word in strs:
                if not word.startswith(res):
                    res = res[:-1]
                    return res
        return res