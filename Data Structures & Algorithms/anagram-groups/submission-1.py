class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = {}
        for s in strs:
            rep = [0] * 26
            for c in s:
                rep[97 - ord(c)] += 1
            if tuple(rep) in s_map:
                s_map[tuple(rep)].append(s)
            else:
                s_map[tuple(rep)] = [s]

        return list(s_map.values())
            