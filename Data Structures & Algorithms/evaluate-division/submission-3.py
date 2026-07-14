class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i, [a, b] in enumerate(equations):
            adjList[a].append([b, values[i]])
            adjList[b].append([a, 1/values[i]])
        
        
        visited = set()

        def dfs(var, target):
            if var not in adjList:
                return -1
            if var in visited:
                return -1
            if var == target:
                return 1
            visited.add(var)

            for nei, val in adjList[var]:
                res = dfs(nei, target)
                if res != -1:
                    visited.remove(var)
                    return val * res
            
            visited.remove(var)
            return -1

        res = []
        for a, b in queries:
            res.append(dfs(a, b))
        return res
        