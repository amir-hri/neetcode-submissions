class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for cour, pre in prerequisites:
            graph[cour].append(pre)
            
        ans = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            ans.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans