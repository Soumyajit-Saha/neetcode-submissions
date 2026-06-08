class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # since we are basically finding diff between each pair of stones, 
        # to find the minimum possible remaining diff, it can be diff between stones in 2 parts
        # One part is the max stones we can get to have a sum nearest to half od total sum
        # Other part is the remaining stones
        # The answer is the diff of these 2
        # So, it is like a 0/1 knapsack problem where we have to find max value for a given weight

        total = sum(stones)
        target = total // 2
        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]

        for i in range(1, len(stones) + 1):
            for j in range(1, target + 1):
                if j >= stones[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return (total - dp[-1][-1]) - dp[-1][-1]
