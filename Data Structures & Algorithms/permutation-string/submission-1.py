class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map_ = {}
        for s in s1:
            map_[s] = map_.get(s, 0) + 1

        k = len(s1)

        l = 0

        map_2 = {}
        for r in range(len(s2)):
            map_2[s2[r]] = map_2.get(s2[r], 0) + 1
            
            if r - l + 1 == len(s1):
                if map_ == map_2:
                    return True
                map_2[s2[l]] -= 1
                if map_2[s2[l]] == 0:
                    map_2.pop(s2[l])
                l += 1
            
        
        return False