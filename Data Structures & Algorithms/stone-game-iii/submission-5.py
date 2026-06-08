class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # At each index if we have either value of (Alice - Bob) or (Bob - Alice), 
    # we can use the value to determine, what will be be the score if Alice or Bob chose the previous 
    # 3 stones. I.E total of those 3 stones + dp[index + 1]
    # So at each index we return (Alice - Bob) or (Bob - Alice)
    # But at index 0 we know it will always be Alice - Bob as Alice starts first

        dp = [float('-inf')] * (len(stoneValue) + 1)
        dp[-1] = 0 # As after last index the value of (Alice - Bob) or (Bob - Alice) is 0

        for i in range(len(stoneValue) - 1, -1, -1):
            total = 0
            res = float('-inf')
            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                # At an index i, We can be either calculating (Alice - Bob) or (Bob - Alice)
                # If at i, we are calculating (Alice - Bob) then dp[j + 1] is (Bob - Alice)
                # Else oposite, but we don't need to care about it.
                res = max(res, total - dp[j + 1])
            dp[i] = res

        return "Tie" if dp[0] == 0 else "Alice" if dp[0] > 0 else "Bob"