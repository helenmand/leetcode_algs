# CORRECT 100%
# Runtime: 40 ms, faster than 76.19% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.4 MB, less than 71.46% of Python3 online submissions for Running Sum of 1d Array.
"""
DESCRIPTION:Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

TEST CASES:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        
        for num in nums[1:]:
            ans.append(ans[-1] + num)
        return ans