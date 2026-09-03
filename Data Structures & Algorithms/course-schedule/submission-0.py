class Solution:
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        graph = {i: [] for i in range(numCourses)}
        for cour, pre in prerequisites:
            graph[cour].append(pre)
        path = set()
        def dfs(course):
            if course in path:
                return False
            if graph[course]==[]:
                return True
            path.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            graph[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True