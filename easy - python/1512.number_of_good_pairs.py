"""
DESCRIPTION:
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
 

TEST CASES:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Input: nums = [1,2,3]
Output: 0
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        
        """
        O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        """
        """
        O(n)
        hm = {}
        for num in nums:
            if num in hm:
                if hm[num] == 1:
                    res += 1
                else:
                    res += hm[num]
                hm[num] += 1
            else:
                hm[num] = 1        
        """
        return res