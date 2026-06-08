class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [float('-inf')] * (len(stoneValue) + 1)
        dp[-1] = 0

        for i in range(len(stoneValue) - 1, -1, -1):
            curr = 0
            for j in range(3):
                if i + j > len(stoneValue) - 1:
                    break
                curr += stoneValue[i + j]
                dp[i] = max(dp[i], curr - dp[i + j + 1])

        return "Alice" if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'