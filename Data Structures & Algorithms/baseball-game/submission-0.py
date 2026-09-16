class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        rec = []
        operations.reverse()
        while operations:
            x = operations.pop()
            if x == 'D':
                x = rec[-1]
                rec.append(int(x) * 2)
            elif x == '+':
                rec.append(int(rec[-1]) + int(rec[-2]))
            elif x == 'C':
                x = rec.pop()
            else:
                rec.append(x)
            print(rec)
        for n in rec:
            res += int(n)
        return res