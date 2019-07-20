# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        curr1 = head
        holder = head.next
        curr2 = holder
        
        while curr1.next and curr2.next:
            curr1.next = curr2.next
            curr1 = curr1.next
            curr2.next = curr1.next
            curr2 = curr2.next
        
        curr1.next = holder
        return head