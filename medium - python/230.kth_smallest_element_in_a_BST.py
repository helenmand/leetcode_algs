"""
DESCRIPTION:
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


TEST CASES:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        q = [root]
        
        while True:
            if len(heap) == k:
                heapq.heappushpop(heap, -q[0].val)
            else:
                heapq.heappush(heap, -q[0].val)
            
            if q[0].right != None:
                q.append(q[0].right)
            if q[0].left != None:
                q.append(q[0].left)
            q.pop(0)
                        
            if not q:
                break
                
        return -heap[0]