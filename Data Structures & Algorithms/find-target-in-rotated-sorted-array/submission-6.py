class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def dfs(l, r):
            if l > r:
                return -1

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # left sorted
                if nums[l] <= target < nums[mid]:
                    return dfs(l, mid-1)
                else:
                    return dfs(mid+1, r)
            else:  # right sorted
                if nums[mid] < target <= nums[r]:
                    return dfs(mid+1, r)
                else:
                    return dfs(l, mid-1)

        return dfs(0, len(nums)-1)
        '''
        # Not right logic
        l = 0
        r = len(nums)-1
        def recurse(l,r):
            if l > r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            if nums[r] < nums[l]:
                if nums[mid] > target:
                    if nums[r] < target:
                        return recurse(l,mid-1)
                    return recurse(mid+1,r)
                if nums[l] > target:
                    return recurse(mid+1,r)
                return recurse(l,mid-1) 
            else:
                if nums[mid] < target:
                    return recurse(mid+1,r)
                return recurse(l,mid-1)
                
        return recurse(l,r)
        '''