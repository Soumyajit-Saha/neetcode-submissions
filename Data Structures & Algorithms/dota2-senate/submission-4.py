class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # We use queue, so that an R can remove the nearest D, and vice versa.
        # Queue gives us that power.
        R = deque()
        D = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == 'R':
                R.append(i)
            else:
                D.append(i)

        while D and R:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                # R will remove a D, and will go to the end of the queue, 
                # so that D can have a chance to remove it later
                R.append(r + n)
            else:
                # Same for D
                D.append(d + n)

        # If R queue is non empty, R wins
        return 'Radiant' if R else 'Dire'
