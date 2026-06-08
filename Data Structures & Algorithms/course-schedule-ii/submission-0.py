class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses) }

        for i in range(len(prerequisites)):
            adjList[prerequisites[i][0]].append(prerequisites[i][1])

        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False

            cycle.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False

            adjList[crs] = []
            res.append(crs)

            visited.add(crs)
            cycle.remove(crs)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return res