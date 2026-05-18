class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def recurse(temp):
            if len(temp) == 1:
                return temp[0]
            s = ''.join(str(x) for x in temp)
            if s in dp:
                return dp[s]
            res = 0
            for i in range(len(temp)):
                if i == 0:
                    res = max(res, temp[i] * temp[i+1] + recurse(temp[1:]))
                elif i == len(temp) - 1:
                    res = max(res, temp[i-1] * temp[i] + recurse(temp[:-1]))
                else:
                    res = max(res, temp[i-1] * temp[i] * temp[i+1] + recurse(temp[:i]+temp[i+1:]))
            dp[s] = res
            return res
        return recurse(nums)
            