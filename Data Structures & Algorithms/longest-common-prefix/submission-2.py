class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for j in range(len(strs)):
                try:
                    if strs[j][i] != temp:
                        return res
                except IndexError:
                    return res
            res += temp
        return res

