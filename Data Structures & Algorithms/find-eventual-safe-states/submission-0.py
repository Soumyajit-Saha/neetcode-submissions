class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        adjList = {i: [] for i in range(n)}
        outdegree = {i: 0. for i in range(n)}

        for i, neis in enumerate(graph):
            for nei in neis:
                adjList[nei].append(i)
                outdegree[i] += 1

        q = Deque()
        for i in range(n - 1, -1, -1):
            if outdegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in adjList[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    q.append(nei)

        return [i for i in range(n) if outdegree[i] == 0]