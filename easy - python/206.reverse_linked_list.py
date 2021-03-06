# CORRECT 100%
# Runtime: 33 ms, faster than 72.46% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.7 MB, less than 44.56% of Python3 online submissions for Reverse Linked List.

"""
DESCRIPTION: Given the head of a singly linked list, reverse the list, and return the reversed list.
Constraints: The number of nodes in the list is the range [0, 5000] & -5000 <= Node.val <= 5000

TEST CASES:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        # 3 pointer solution
        prevNode = None
        currentNode = head
        nextNode = None
        
        while currentNode is not None:            
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        head = prevNode
        return head