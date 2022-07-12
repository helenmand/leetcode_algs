# CORRECT 100% 
# Runtime: 220 ms, faster than 23.67% of Python3 online submissions for Missing Number.
# Memory Usage: 15.4 MB, less than 79.61% of Python3 online submissions for Missing Number.

"""
DESCRIPTION: Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Constraints: n == nums.length & 1 <= n <= 104 & 0 <= nums[i] <= n & All the numbers of nums are unique.


TEST CASES:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
1 is the missing number in the range since it does not appear in nums.

 
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (sum(range(len(nums) + 1)) - sum(nums))