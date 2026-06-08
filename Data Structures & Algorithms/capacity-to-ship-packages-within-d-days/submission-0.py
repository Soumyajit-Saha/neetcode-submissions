class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        res = 0

        def canShip(maxWeight):
            ship_days = 0
            curr = 0
            for w in weights:
                curr += w
                if curr > maxWeight:
                    curr = w
                    ship_days += 1
            return ship_days + 1 <= days

        while l <= r:
            mid = l + (r - l) // 2
            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res