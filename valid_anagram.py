# CORRECT 100%
# Runtime: 32 ms, faster than 98.46% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.7 MB, less than 32.12% of Python3 online submissions for Valid Anagram.

"""
DESCRIPTION: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Constraints: 1 <= s.length, t.length <= 5 * 104 & s and t consist of lowercase English letters.


TEST CASES:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # picking the sting with the most character.
        s,t = (s,t) if len(s)>=len(t) else (t,s)
        
        # while string has characters.
        while s:
            # checking every time for the 1st char
            # because we remove it afterwards.
            char = s[0]
            
            # if the char is not in both strings the 
            # same times it cant be an anagram.
            if s.count(char) != t.count(char):
                return False
            
            # removing the character from the strings.
            s = s.replace(char,'')
            t = t.replace(char,'')
        return True