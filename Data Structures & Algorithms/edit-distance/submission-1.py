class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #recursively try all possiblities for each step and then get the min steps needed
        dp = {}
        def recurse(temp1, temp2):
            if (temp1,temp2) in dp:
                return dp[(temp1,temp2)]
            if not temp1:
                return len(temp2)
            if not temp2:
                return len(temp1)
            if temp1[0] == temp2[0]:
                res = recurse(temp1[1:],temp2[1:])
            else:
                res =  1 + min(recurse(temp1,temp2[1:]),
                            recurse(temp1[1:],temp2), 
                            recurse(temp1[1:], temp2[1:]))
            dp[(temp1,temp2)] = res
            return res
        return recurse(word1,word2)
            
            
            
