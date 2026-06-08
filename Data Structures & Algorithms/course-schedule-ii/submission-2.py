class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
            indegree[pre] += 1

        queue = deque()
        res = []
        for i, deg in indegree.items():
            if deg == 0:
                queue.append(i)

        while queue:
            crs = queue.popleft()
            for pre in adjList[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
            res.append(crs)

        if len(res) != numCourses:
            return []
        else:
            return res[::-1]
