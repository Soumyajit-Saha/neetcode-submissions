class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjList = defaultdict(list)
        for n1, n2 in edges:
            adjList[n2].append(n1)
            adjList[n1].append(n2)

        edgeCount = {}
        queue = deque()
        for node, nei in adjList.items():
            edgeCount[node] = len(nei)
            if edgeCount[node] == 1:
                queue.append(node)

        while queue:
            if n <= 2:
                return list(queue)
            size = len(queue)
            while size:
                node = queue.popleft()
                n -= 1
                for nei in adjList[node]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        queue.append(nei)
                size -= 1
