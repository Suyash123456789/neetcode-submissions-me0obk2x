class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(i):
            if preMap[i] == []:
                return True
            if i in visit:
                return False

            visit.add(i)
            for j in preMap[i]:
                if not dfs(j):
                    return False
            visit.remove(i)
            preMap[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


