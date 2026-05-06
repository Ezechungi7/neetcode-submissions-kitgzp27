class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        res = []
        def dfs(crs):
            if crs in visit:
                return False # Loop detected
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            if crs not in res:
                res.append(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return list(res)



