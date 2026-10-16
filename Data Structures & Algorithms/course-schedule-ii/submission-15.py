class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, path = set(), set()

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True

            path.add(i)
            for j in preMap[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            visit.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res 