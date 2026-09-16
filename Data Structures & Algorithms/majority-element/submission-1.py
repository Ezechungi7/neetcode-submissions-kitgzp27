class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        m = 0
        for n in nums:
            d[n] += 1
            if m < d[n]:
                res = n
                m = d[n]
            
        return res