class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topoSort(edges):
            indegree = {i: 0 for i in range(1, k + 1)}
            adjList = {i: [] for i in range(1, k + 1)}

            for u, v in edges:
                adjList[u].append(v)
                indegree[v] += 1

            q = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            res = []
            while q:
                node = q.popleft()
                res.append(node)
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

            return res

        rowOrder = topoSort(rowConditions)
        if len(rowOrder) != k: return []

        colOrder = topoSort(colConditions)
        if len(colOrder) != k: return []

        rowMap = {}
        colMap = {}

        for i, r in enumerate(rowOrder):
            rowMap[r] = i

        for i, c in enumerate(colOrder):
            colMap[c] = i

        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            res[rowMap[i]][colMap[i]] = i

        return res

