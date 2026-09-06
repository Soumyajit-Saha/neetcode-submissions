class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sources = []
        destinations = []

        for n, u, v in trips:
            sources.append([u, n])
            destinations.append([v, n])

        sources.sort()
        destinations.sort()

        i1 = 0
        i2 = 0
        currPass = 0

        while i1 < len(sources) and i2 < len(destinations):
            if sources[i1][0] < destinations[i2][0]:
                currPass += sources[i1][1]
                if currPass > capacity:
                    return False
                i1 += 1
            else:
                currPass -= destinations[i2][1]
                i2 += 1
        
        return True

        