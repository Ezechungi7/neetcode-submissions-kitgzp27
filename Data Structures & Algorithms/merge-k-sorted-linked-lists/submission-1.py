# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        curr = ListNode()
        res = curr
        firsts = []
        for i in range(len(lists)):
            firsts.append([lists[i].val,i])
        heapq.heapify(firsts)
        #value, idx = firsts[0][0], firsts[0][1]
        while True:
            # lists[firsts[0][1]] is current linked list 
            # we need to update firsts as well after adding and moving to next
            if not firsts:
                break
            curr.val = firsts[0][0]
            #res.append(firsts[0][0]) # add smallest element
            try:
                lists[firsts[0][1]] = lists[firsts[0][1]].next #go to the next in the respective list
            except AttributeError:
                pass
            if lists[firsts[0][1]]:
                heapq.heappush(firsts,[lists[firsts[0][1]].val,firsts[0][1]]) #push that next value
            heapq.heappop(firsts) #pop what we appended (smallest)
            if firsts:
                curr.next = ListNode()
                curr = curr.next
        return res


