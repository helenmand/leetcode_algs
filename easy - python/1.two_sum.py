"""
DESCRIPTION:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 
TEST CASES:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Input: nums = [-1,-2,-3,-4,-5], target = -8
Output: [2,4]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [-1,0]
        
        while nums:
            num = nums.pop(0)
            res[0] += 1
            
            if target - num in nums:
                res[1] = nums.index(target - num) + res[0] + 1
                return res