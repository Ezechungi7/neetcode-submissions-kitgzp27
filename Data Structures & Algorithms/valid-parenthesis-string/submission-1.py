class Solution:
    def checkValidString(self, s: str) -> bool:
        #stack = []
        dp = {}
        def recurse(word,left):
            if left < 0:
                return False
            if not word:
                return left == 0
            state = (word,left)
            if state in dp:
                return dp[state]
            if word[0] == '(':
                left += 1
                print(left)
                dp[state] = recurse(word[1:], left)
                return dp[state]
            if word[0] == ')':
                if left == 0:
                    dp[state] = False
                    return dp[state]
                left -= 1
                print(left)
                dp[state] = recurse(word[1:], left)
                return dp[state]
            if word[0] == '*':
                dp[state] = recurse(word[1:],left) or recurse(word[1:], left+1) or recurse(word[1:], left-1)
                return dp[state]
            #return dp[(word,left)]
        return recurse(s,0)

