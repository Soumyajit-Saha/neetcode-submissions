class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        res = 0

        while l <= r:
            heaviestPerson = people[r]
            lightestPerson = people[l]

            if heaviestPerson + lightestPerson > limit:
                # Only add heaviest to the boat
                r -= 1
                res += 1
            else:
                # Add both to the boat
                r -= 1
                l += 1
                res += 1

        return res

