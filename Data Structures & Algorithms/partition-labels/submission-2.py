class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i in range(len(s)):
            index[s[i]] = i

        res = []
        size = 0
        end = -1
        for i in range(len(s)):
            end = max(end, index[s[i]])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        
        return res
