"""
DESCRIPTION:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


TEST CASES:
Input: root = [1,2,2,3,4,4,3]
Output: true
Explanation:
          1
       /  |  \
      2   |   2
     / \  |  / \
    3   4 | 4   3

Input: root = [1,2,2,null,3,null,3]
Output: false
Explanation:
          1
       /  |  \
      2   |   2
       \  |    \
        3 |     3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricSubTree(root.right, root.left)
        
    def isSymmetricSubTree(self, right: Optional[TreeNode], left: Optional[TreeNode]) -> bool:
        if not right and not left:
            return True
        if not right or not left:
            return False
        
        if right.val != left.val:
            return False
        else:
            rightLeft = self.isSymmetricSubTree(right.right, left.left)
            leftRight = self.isSymmetricSubTree(right.left, left.right)
            
            return leftRight and rightLeft