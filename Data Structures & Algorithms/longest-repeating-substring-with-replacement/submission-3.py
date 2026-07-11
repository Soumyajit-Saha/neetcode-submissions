class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_ = 0
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_ = max(max_, count[s[r]])

            size = r - l + 1
            if size - max_ <= k:
                res = max(res, size)

            if size - max_ > k:
                count[s[l]] -= 1
                max_ = max(count.values())
                l += 1
        
        return res