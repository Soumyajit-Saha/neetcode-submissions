class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Intuition is to start check from leaf nodes and come towards the center
        # The leaf nodes are the ones that have 1 edge from them
        # As we go from leaf nodes to inside, decrease the edge count of the node and now they become the leaf node, and decrement the total node count
        # Perform level order bfs search from leaf nodes
        # Go until until there is atmost 2 nodes (it came from going over many examples)
        if n == 1:
            # this will be the leaf node without an edge and our algo will fail
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