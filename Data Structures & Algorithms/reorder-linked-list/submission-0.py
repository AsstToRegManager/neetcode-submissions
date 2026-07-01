# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_head = slow.next
        prev = slow.next = None
        while new_head:
            tmp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = tmp
        
        new_head = prev
        first = head
        while new_head and first:
            tmp1 = first.next
            tmp2 = new_head.next

            first.next = new_head
            new_head.next = tmp1

            first = tmp1
            new_head = tmp2
        
