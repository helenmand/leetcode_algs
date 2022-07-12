# CORRECT 100%
# Runtime: 1176 ms, faster than 13.39% of Python3 online submissions for Single Number.
# Memory Usage: 16.6 MB, less than 59.02% of Python3 online submissions for Single Number.

"""
DESCRIPTION: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


TEST CASES:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # this array helps to keep track of the duplicate numbers
        ans = []
        
        # checking every number of the array
        for number in nums:
            # finding a number that has already been added to the 
            # assisting array means that we can remove this number
            # because we found its duplicate
            if number in ans:
                ans.remove(number)
            # otherwise we add the number to the ans array 
            else:
                ans.append(number)
        # since there is only one answer, it is the only element of the ans array.
        # return the item because int is expected [not list]   
        return ans[0]