class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = []
        resLen = float('inf')

        t_map = {}

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        need = len(t_map)
        have = 0

        l = 0

        s_map = {}
        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1

            if s[r] in t_map and t_map[s[r]] == s_map[s[r]]:
                have += 1

                if have == need:
                    if resLen > r - l + 1:
                        resLen = r - l + 1
                        res = [l, r]

                while have == need:
                    if resLen > r - l + 1:
                        resLen = r - l + 1
                        res = [l, r]
                    s_map[s[l]] -= 1
                    if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                        have -= 1
                    l += 1

        return s[res[0]: res[1] + 1] if resLen != float('inf') else ''