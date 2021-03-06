# CORRECT 100%
# Runtime: 59 ms, faster than 15.14% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.7 MB, less than 60.64% of Python3 online submissions for Delete Node in a Linked List.

"""
DESCRIPTION: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.


TEST CASES:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Input: head = [1,2,3,4], node = 3
Output: [1,2,4]

Input: head = [0,1], node = 0
Output: [1]

Input: head = [-3,5,-99], node = -3
Output: [5,-99]

Input: head = [2,0,1,3], node = 2
Output: [0,1,3]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # replacing data of the deleting node with its next node.  
        node.val = node.next.val
        node.next = node.next.next
        