class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
        '''
        correct = [i for i in range(len(nums)+1)]
        #print(correct)
        return list(set(correct) - set(nums))[0]
        '''
        '''
        nums.sort()
        try:
            for i in range(len(nums)+1):
                if i != nums[i]:
                    return i
        except:
            return len(nums)
        '''