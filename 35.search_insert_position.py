# CORRECT 100%
# Runtime: 53 ms, faster than 31.64% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.3 MB, less than 24.06% of Python3 online submissions for Search Insert Position.
 
"""
DESCRIPTION:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
    * 1 <= nums.length <= 104
    * -104 <= nums[i] <= 104
    * nums contains distinct values sorted in ascending order.
    * -104 <= target <= 104


TEST CASES:
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
 
        while low <= high:

            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid 
   
        return low