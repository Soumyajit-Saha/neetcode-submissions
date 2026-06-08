class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = {i: [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for adjNode in adjList[node]:
                if adjNode == parent:
                    continue
                if dfs(adjNode, node) == False:
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n