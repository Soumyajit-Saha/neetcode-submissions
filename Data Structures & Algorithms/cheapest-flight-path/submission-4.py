class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp_dp = dp.copy()
            for edge in flights:
                u = edge[0]
                v = edge[1]
                cost = edge[2]
                if dp[u] == float('inf'):
                    continue
                temp_dp[v] = min(temp_dp[v], cost + dp[u])

            dp = temp_dp
        
        return -1 if dp[dst] == float('inf') else dp[dst]
