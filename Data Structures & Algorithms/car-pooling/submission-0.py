class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        src = []
        dst = []

        for numPass, s, d in trips:
            src.append((s, numPass))
            dst.append((d, numPass))


        i = 0
        j = 0

        currPass = 0
        while i < len(src) and j < len(dst):
            if src[i][0] < dst[j][0]:
                currPass += src[i][1]
                i += 1
            else:
                currPass -= dst[j][1]
                j += 1
            if currPass > capacity:
                return False

        while j < len(dst):
            currPass -= dst[j][1]
            j += 1
            if currPass > capacity:
                return False

        return True