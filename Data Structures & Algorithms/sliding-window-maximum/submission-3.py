class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
        