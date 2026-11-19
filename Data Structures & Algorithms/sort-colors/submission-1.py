class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        res = []
        for num in nums:
            count[num] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                res.append(i)
        nums[:] = res.copy()
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        