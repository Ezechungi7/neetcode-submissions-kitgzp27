class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # what should the 2d dp table represent?
        dp = [[-1] * (len(s2)+1) for _ in range(len(s1)+1)]

        def recurse(i,n,m):
            if i == len(s3):
                return (n == len(s1)) and (m == len(s2))
            if dp[n][m] != -1:
                return dp[n][m]
            
            res = False
            if n < len(s1) and s1[n] == s3[i]:
                res = recurse(i+1,n+1,m)
            if not res and m < len(s2) and s2[m] == s3[i]:
                res = recurse(i+1,n,m+1)
            dp[n][m] = res
            return res
        return recurse(0,0,0)
        
