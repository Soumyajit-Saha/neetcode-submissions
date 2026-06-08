class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        map_ = {s[0]: 0}
        res = 1

        start = 0

        for r in range(1, len(s)):
            if s[r] not in map_:
                res = max(res, r - start + 1)
            else:
                for k in range(start, map_[s[r]]):
                    map_.pop(s[k], None)
                start = map_[s[r]] + 1
            map_[s[r]] = r

        return res