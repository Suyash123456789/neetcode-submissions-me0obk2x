class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={ c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output=[]
        visit, cycle=set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output