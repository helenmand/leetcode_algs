# CORRECT 100%
#Runtime: 32 ms, faster than 86.32% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 14.1 MB, less than 72.47% of Python3 online submissions for Sum of Unique Elements.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if nums.count(num) == 1:
                sum += num
        return sum