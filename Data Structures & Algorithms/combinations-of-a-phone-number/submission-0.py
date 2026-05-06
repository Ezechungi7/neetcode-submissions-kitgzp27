class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        representations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz" 
        }
        res = []
        temp = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(temp))
                return
            for c in representations[digits[i]]:
                temp.append(c)
                backtrack(i+1)
                temp.pop()
        backtrack(0)
        return res
    
