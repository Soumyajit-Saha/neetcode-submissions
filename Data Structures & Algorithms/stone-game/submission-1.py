class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l, r):
            # return the max Score Alice can get
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            # If size of the piles is odd, then we are in Bob's turn, 
            # So, we don't want to add Bob's score as we are only bothered about Alice score
            bob_turn = ((r - l) + 1) % 2 == 1
            left = piles[l] if bob_turn else 0
            right = piles[r] if bob_turn else 0
            res = max(left + dfs(l + 1, r), dfs(l, r - 1) + right)
            dp[(l, r)] = res
            return dp[(l, r)]

        alice = dfs(0, len(piles) - 1)
        bob = sum(piles) - alice
        return True if alice > bob else False