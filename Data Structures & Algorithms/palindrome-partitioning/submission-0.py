class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispal(mystr):
            return mystr == mystr[::-1]
        # Compute all possible substrings
        # Compute all possible palindromes from those substrings
        subsets = []
        subset = []
        def backtrack(j,i):
            if i >= len(s):
                if i == j:
                    subsets.append(subset.copy())
                return
            if ispal(s[j:i+1]):
                subset.append(s[j:i+1])
                backtrack(i+1,i+1)
                subset.pop()
            backtrack(j,i+1)
        

        backtrack(0,0)
        return subsets

            
        