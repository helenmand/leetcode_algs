# CORRECT 100%
#Runtime: 32 ms, faster than 86.32% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 14.1 MB, less than 72.47% of Python3 online submissions for Sum of Unique Elements.
"""
DESCRIPTION:
You are given an integer array nums. The unique elements of an array 
are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.


TEST CASES:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
"""
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if nums.count(num) == 1:
                sum += num
        return sum