class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        elif k >= len(nums):
            return [max(nums)]
        res = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            if i >= k-1:
                while heap[0][1] <= i-k: #because the window goes from i-k to i, so window size is k
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
        '''
        #BRUTE FORCE
        if not nums:
            return []
        elif k >= len(nums):
            return [max(nums)]
        res = []
        l = 0
        r = k
        while r <= len(nums):
            #print(nums[l:r])
            res.append(max(nums[l:r]))
            l += 1
            r += 1
        return res
        '''
        