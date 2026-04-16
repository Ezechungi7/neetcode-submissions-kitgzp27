# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        now = 1
        curr = head
        prev = None
        while now < left:
            prev = curr
            curr = curr.next  
            now += 1
        
        first = prev
        subfirst = curr
        while now < right:
            
        last = curr
        first.next = last
        return head
        '''
        now = 1
        curr = head
        prev = None

        # Step 1: move to "left"
        while now < left:
            prev = curr
            curr = curr.next
            now += 1

        first = prev          # node before sublist
        tail = curr           # will become tail after reversal

        # Step 2: reverse
        prev = None
        while now <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            now += 1

        last = prev           # new head of reversed sublist

        # Step 3: reconnect
        if first:
            first.next = last
        else:
            head = last       # left == 1 case

        tail.next = curr

        return head