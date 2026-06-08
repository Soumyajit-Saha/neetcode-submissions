class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = Counter(s1)

        l = 0

        map2 = {}

        for r in range(len(s2)):
            map2[s2[r]] = 1 + map2.get(s2[r], 0)

            if r - l + 1 == len(s1):
                if map2 == map1:
                    return True
                else:
                    map2[s2[l]] -= 1
                    if map2[s2[l]] == 0:
                        map2.pop(s2[l], None)
                    l += 1
        
        return False