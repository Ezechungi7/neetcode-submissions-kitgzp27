class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for w in strs:
            temp = '~'
            for c in w:
                temp += str(ord(c)) + '_'
            res += temp
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        temp = ''
        now = ''
        for i in range(1,len(s)):
            if s[i] == '~':
                res.append(temp)
                temp = ''
            elif s[i] == '_':
                temp += chr(int(now))
                now = ''
                continue
            else:
                now += s[i]
        res.append(temp)
                
        return res
