class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        try:
            for i in range(len(nums)+1):
                if i != nums[i]:
                    return i
        except:
            return len(nums)