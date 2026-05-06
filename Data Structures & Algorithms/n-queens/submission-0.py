class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        sol = ["." * n for _ in range(n)] 
        print(sol)
        def valid(i,j,user_list):
            for r in range(len(user_list)):
                for c in range(len(user_list[r])):
                    if user_list[r][c] == 'Q':
                        if r == i or c == j:
                            return False
                        if abs(r-i) == abs(c-j): #if they move the same steps horizontally and vertically, then they are in the same diagonal
                            return False
            return True


        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return
            for j in range(len(sol[i])):
                if valid(i,j,sol):
                    old_row = sol[i]
                    sol[i] = "." * j + 'Q' + "." * (n-j-1)
                    backtrack(i+1)
                    sol[i] = old_row
        backtrack(0)
        return res


