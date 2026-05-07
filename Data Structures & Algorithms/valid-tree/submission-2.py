class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if detect cycle then false else true
        # if not connected return false else true
        if len(edges) > n-1:
            return False
        nodemap = {i:[] for i in range(n)}
        for source, dest in edges:
            nodemap[source].append(dest)
            nodemap[dest].append(source)
        visit = set()

        def dfs(s,prev):
            if s in visit:
                return False
            visit.add(s)

            for d in nodemap[s]:
                if d == prev:
                    continue
                if not dfs(d,s):
                    return False
            return True
        return dfs(0,-1) and len(visit) == n