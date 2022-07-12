# CORRECT 100%
# Runtime: 84 ms, faster than 80.85% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 14.6 MB, less than 53.58% of Python3 online submissions for Concatenation of Array.
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * 2*n
        
        for i,num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num

        return ans