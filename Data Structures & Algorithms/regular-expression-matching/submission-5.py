class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recurse(i,j):
            if j == len(p):
                return i == len(s)
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )
            if j + 1 < len(p) and p[j + 1] == '*':

                return (
                    recurse(i, j + 2) or      # skip x*
                    (first_match and recurse(i + 1, j))
                )

            # normal match
            return first_match and recurse(i + 1, j + 1)

        return recurse(0, 0)