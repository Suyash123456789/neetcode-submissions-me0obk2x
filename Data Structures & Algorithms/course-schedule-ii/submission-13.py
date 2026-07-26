class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        res = []
        visited, path = set(), set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in path:
                return False
            path.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
