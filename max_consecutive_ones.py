# CORRECT 100%
# Weekly challenge september 21, 2021

"""
DESCRIPTION: Given a binary array nums, return the maximum number of consecutive 1's in the array.
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.


TEST CASES:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # FASTER 
        # Runtime: 332 ms
        # Memory Usage: 14.5 MB
        max = -1
        temp = 0
        for i in range(0, len(nums)):
            if nums[i]:
                temp = temp + 1
            else:
                if temp>max:
                    max = temp
                temp = 0
        if temp>max:
            return temp
        return max
        
        """
        # solution no. 2
        # Runtime: 352 ms
        # Memory Usage: 14.4 MB
        max = 0
        temp = 0
        
        for number in nums:
            temp = temp + number
            max = temp if temp > max else max
            if number == 0:
                temp = number
                
        return max
        """