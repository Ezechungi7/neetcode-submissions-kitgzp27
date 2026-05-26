class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def recurse(i,j):
            if j == len(p):
                return i == len(s)
            if (i,j) in dp:
                return dp[(i,j)]
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[(i,j)] = (
                    recurse(i, j + 2) or      # skip x*
                    (first_match and recurse(i + 1, j))
                )
                return dp[(i,j)]

            # normal match
            dp[(i,j)] = first_match and recurse(i + 1, j + 1)
            return dp[(i,j)]

        return recurse(0, 0)