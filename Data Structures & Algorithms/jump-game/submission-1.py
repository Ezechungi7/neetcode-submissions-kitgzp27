class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True
        return True
        
        '''
        i = 0
        while i < len(nums)-1:
            temp = nums[i]
            for num in nums[i:i+nums[i]+1]:
                if temp < num:
                    temp = num
                
            print(temp)   
            if temp == 0:
                return False
            i += temp
        return True
        '''