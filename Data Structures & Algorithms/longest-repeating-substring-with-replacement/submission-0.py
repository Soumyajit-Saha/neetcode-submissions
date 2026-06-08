class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l = 0
        map_= {s[l]: 1}
        max_ = 1
        for r in range(1, len(s)):
            map_[s[r]] = map_.get(s[r], 0) + 1
            if map_[s[r]] > max_:
                max_ = map_[s[r]]

            if r - l + 1 - max_ <= k:
                res = max(res, r - l + 1)

            if r - l + 1 - max_ > k:
                while r - l + 1 - max_ > k:
                    map_[s[l]] -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
