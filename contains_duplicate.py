# CORRECT 100% 

"""
DESCRIPTION: Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.
Constraints: 1 <= nums.length <= 105 & -109 <= nums[i] <= 109


TEST CASES:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # sets do not contain duplicates
        # if there is a value more than once in the nums list,
        # it will be included once in the set.
        # so the set, will have smaller lenght. 
        setLen = len(set(nums))
        listLen = len(nums)
        
        # if the lenghts are not equal, the list has
        # values that appear multiple times. 
        return listLen != setLen