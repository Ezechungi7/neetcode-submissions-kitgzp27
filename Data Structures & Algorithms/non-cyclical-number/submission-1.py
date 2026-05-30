class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        history.add(n)
        while True:
            if n == 1:
                return True
            s = str(n)
            n = 0
            for c in s:
                n += int(c)**2
            if n in history:
                return False
            history.add(n)

            