# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        now = 1
        curr = head
        prev = None
        while now < left:
            prev = curr
            curr = curr.next  
            now += 1
        
        first = prev
        tail = curr
        prev = None
        while now <= right:
            next_now = curr.next
            curr.next = prev
            prev = curr
            curr = next_now
            now += 1
        if first:
            first.next = prev
        else:
            head = prev
        tail.next = curr
        return head
        