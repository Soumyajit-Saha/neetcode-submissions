class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if dfs(nei, node) == False:
                    return False
            return True

        res = dfs(0, -1)
        if len(visit) == n:
            return res
        else:
            return False