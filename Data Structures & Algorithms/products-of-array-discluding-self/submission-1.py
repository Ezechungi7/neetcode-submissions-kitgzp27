class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        numofzeros = 0
        prod = 1
        prod2 = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                numofzeros += 1
        for n in nums:
            if n == 0:
                prod = prod*n
                continue
            prod = prod*n
            prod2 = prod2*n
        if numofzeros > 1:
            prod2 = 0
        for n in nums:
            if n == 0:
                res.append(prod2)
            else:
                res.append(int(prod/n))
        return res
        
        '''
        # BRUTE FORCE
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                prod = prod*nums[j]
            res.append(prod)
        return res
        '''
        