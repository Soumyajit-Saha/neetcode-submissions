class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        adjList = {i: [] for i in range(1, k + 1)}
        indegree = {i: 0 for i in range(1, k + 1)}
        
        for pre, val in rowConditions:
            adjList[pre].append(val)
            indegree[val] += 1

        q = deque()
        for val, deg in indegree.items():
            if deg == 0:
                q.append(val)

        row = []

        while q:
            node = q.popleft()
            row.append(node)
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        adjList = {i: [] for i in range(1, k + 1)}
        indegree = {i: 0 for i in range(1, k + 1)}
        
        for pre, val in colConditions:
            adjList[pre].append(val)
            indegree[val] += 1

        q = deque()
        for val, deg in indegree.items():
            if deg == 0:
                q.append(val)

        col = []

        while q:
            node = q.popleft()
            col.append(node)
            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        print(row, col)
        if len(row) != k or len(col) != k:
            return []

        rowMap = {}
        colMap = {}

        for i, r in enumerate(row):
            rowMap[r] = i

        for i, c in enumerate(col):
            colMap[c] = i

        res = [[0] * k for _ in range(k)]

        for i in range(1, k + 1):
            res[rowMap[i]][colMap[i]] = i

        return res
        

        

        