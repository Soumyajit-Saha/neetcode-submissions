class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = {i: 0 for i in range(n)}

        if n == 1:
            return [0]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)

        k = n
        while q:
            if k <= 2:
                return list(q)
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                k -= 1
                for nei in adjList[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
