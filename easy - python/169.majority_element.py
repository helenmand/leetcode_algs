# CORRECT 100%
"""
DESCRIPTION: Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Constraints: n == nums.length & 1 <= n <= 5 * 104 & -231 <= nums[i] <= 231 - 1
 

TEST CASES:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]