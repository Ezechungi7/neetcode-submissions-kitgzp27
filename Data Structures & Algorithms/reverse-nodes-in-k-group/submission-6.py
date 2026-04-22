# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        counter = 0
        pos_counter = head
        while pos_counter:
            counter += 1
            pos_counter = pos_counter.next
        if counter < k:
            return head
        
        prev = None
        curr = head

        for _ in range(k):
            nextnow = curr.next
            curr.next = prev
            prev = curr
            curr = nextnow
        #second_half = curr
        if counter - k < k:
            head.next = curr
            return prev
        # if not then
        head.next = curr
        final_head = prev
        #----------
        #last = head
        #head_next_half = curr
        #last_first_half = head
        for _ in range((counter//k)-1):
            last_first_half = head
            head_next_half = curr #head
            prev = None
            for _ in range(k):
                nextnow = curr.next
                curr.next = prev
                prev = curr
                curr = nextnow
            head_next_half.next = curr
            last_first_half.next = prev
            head = head_next_half

        return final_head


        