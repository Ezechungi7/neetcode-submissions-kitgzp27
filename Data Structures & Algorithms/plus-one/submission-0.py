class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for n in digits:
            s += str(n)
        print(s)
        res = int(s) + 1
        final = []
        for c in str(res):
            final.append(int(c))
        return final