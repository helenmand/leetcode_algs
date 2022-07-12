# CORRECT 100%
# Runtime: 1220 ms, faster than 5.08% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.5 MB, less than 80.71% of Python3 online submissions for First Unique Character in a String.

"""
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


TEST CASES:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = s.lower()
        
        # COULD BE BETTER
        for letter in clean_s:
            if not letter.isalnum():
                clean_s = clean_s.replace(letter, "")
                
        return clean_s == clean_s[::-1]
       