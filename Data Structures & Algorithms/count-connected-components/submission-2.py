class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj  = {i:[] for i in range(n)}
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        visit = [False] * n
        def dfs(s):
            for d in adj[s]:
                if not visit[d]:
                    visit[d] = True
                    dfs(d)
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res += 1
        return res


        '''
        heapq.heapify(edges)
        temp = set()
        res = 0
        nodes = set()
        print(nodes)
        for _ in range(len(edges)):
            if edges[0][0] in temp or edges[0][1] in temp:
                temp.add(edges[0][0])
                temp.add(edges[0][1])
                nodes.add(edges[0][0])
                nodes.add(edges[0][1])
                heapq.heappop(edges)
            else:
                temp.clear()
                temp.add(edges[0][0])
                temp.add(edges[0][1])
                nodes.add(edges[0][0])
                nodes.add(edges[0][1])
                res += 1
                heapq.heappop(edges)
        return res + n - len(nodes)
        '''

