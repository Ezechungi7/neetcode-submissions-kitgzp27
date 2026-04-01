class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        def recurse(l,r,last):
            if last < nums[r]:
                return last
            if l >= r:
                return nums[r]
            mid = (l + r)//2 + 1
            print(mid)
            if nums[mid] < nums[l]:
                return recurse(l,mid-1,nums[mid])
            if nums[r] < nums[mid]:
                return recurse(mid,r-1,nums[r])
            if nums[l] < nums[mid]:
                return recurse(l+1,mid,nums[l])
            
        return recurse(l,r,nums[r])