# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        
        prev, curr = head, head.next
        head.next = None
        
        while curr.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr.next = prev
        return curr
            