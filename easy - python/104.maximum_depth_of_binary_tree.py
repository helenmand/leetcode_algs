"""
DESCRIPTION: Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


TEST CASES:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Input: root = []
Output: 0

Input: root = [0]
Output: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # tree is empty
        if root is None:
            return 0
        
        # calling function for the left & right subtree
        left = self.maxDepth( root.left)
        right = self.maxDepth( root.right)
        
        # getting the maximun depth plus the root
        if left > right:
            return left + 1
        else:
            return right + 1