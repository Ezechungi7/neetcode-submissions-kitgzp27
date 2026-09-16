class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        res = 0
        m = 0
        for k in d:
            if d[k] > m:
                m = d[k]
                res = k
        return res