class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        visited, path = set(), set()
        output = []
        def dfs(crs):
            if crs in path:
                return False

            if crs in visited:
                return True

            path.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return output

