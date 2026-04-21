class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        elif k >= len(nums):
            return [max(nums)]
        res = []
        neg = []
        for n in nums:
            neg.append(-n)
        l = 0
        r = k
        while r <= len(nums):
            temp = neg[l:r]
            heapq.heapify(temp)
            res.append(-temp[0])
            l += 1
            r += 1
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
        