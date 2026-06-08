class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = h
        while l <= r:
            mid = l + (r - l) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / mid)

            if totalTime == h:
                r = mid - 1
                res = mid

            elif totalTime > h:
                l = mid + 1
            
            else:
                r = mid - 1
                res = mid

        return res