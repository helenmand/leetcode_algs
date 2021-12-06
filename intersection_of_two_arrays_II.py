# CORRECT 100% 
# Runtime: 80 ms, faster than 21.41% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.5 MB, less than 10.39% of Python3 online submissions for Intersection of Two Arrays II.

"""
DESCRIPTION:Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Constraints: 1 <= nums1.length, nums2.length <= 1000 & 0 <= nums1[i], nums2[i] <= 1000


TEST CASES:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        search_set = set(nums1) if len(set(nums1)) > len(set(nums2)) else set(nums2)
        ans = []    
            
        for element in search_set:
            if (element in nums2) and (element in nums1):
                ans.extend(repeat(element, min(nums1.count(element), nums2.count(element))))
                
        return ans