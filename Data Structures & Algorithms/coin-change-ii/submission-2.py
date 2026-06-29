class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    continue
                dp[j] += dp[j - coins[i]]

        print(dp)
        return dp[-1]
