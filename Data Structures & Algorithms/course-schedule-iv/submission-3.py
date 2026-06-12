class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # Build adjacency list: course -> its direct prerequisites
        adj = defaultdict(list)
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        # Cache: course -> ALL its prerequisites (direct + transitive)
        allPrereqs = {}

        def dfs(course):
            if course not in allPrereqs:
                allPrereqs[course] = set()
                for prereq in adj[course]:
                    allPrereqs[course] |= dfs(prereq)   # collect prereq's prereqs
                allPrereqs[course].add(course)           # include itself

            return allPrereqs[course]

        # Populate cache for every course
        for course in range(numCourses):
            dfs(course)

        # For each query (u, v): is u a prerequisite of v?
        return [u in allPrereqs[v] for u, v in queries]