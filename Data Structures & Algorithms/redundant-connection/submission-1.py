class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        def countComponents(temp_edges):

            adj = {i: [] for i in range(1, n + 1 )}

            for s, d in temp_edges:
                adj[s].append(d)
                adj[d].append(s)

            visit = [False] * (n + 1)

            def dfs(s):
                for d in adj[s]:
                    if not visit[d]:
                        visit[d] = True
                        dfs(d)


            res = 0

            for node in range(1, n + 1):
                if not visit[node]:
                    visit[node] = True
                    dfs(node)
                    res += 1

            return res

        result = []

        for i in range(len(edges)):
            temp = edges[:i] + edges[i + 1:]

            if countComponents(temp) == 1:
                result = edges[i]

        return result