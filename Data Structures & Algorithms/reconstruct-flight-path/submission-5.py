class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm
        # To find an Euler circuit
        # To go through all the edges in a graph exactly once
        
        adjList = defaultdict(deque)
        for src, dst in sorted(tickets):
            adjList[src].append(dst)

        res = []
        def dfs(node):
            while adjList[node]:
                nxt = adjList[node].popleft()
                dfs(nxt)
            res.append(node)

        # return reversed res
        dfs('JFK')
        return res[::-1]