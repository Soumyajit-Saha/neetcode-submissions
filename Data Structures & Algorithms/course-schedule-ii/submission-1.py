class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
            indegree[pre] += 1

        queue = deque()
        visited = set()
        res = []
        for i, deg in indegree.items():
            if deg == 0:
                queue.append(i)

        while queue:
            crs = queue.popleft()
            if crs in visited:
                continue
            for pre in adjList[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
            res.append(crs)
            visited.add(crs)

        if len(visited) != numCourses:
            return []
        else:
            return res[::-1]
