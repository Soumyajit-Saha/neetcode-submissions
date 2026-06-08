class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Idea is to store the last index of all the chars in s
        # Traverse s again
        # maintain an end value which is the end value of the ongoing substring and the size of the ongoing substring
        # for each char get its last index, so end value becomes max of prev end value and the last index
        # if you reach an end value, save the substring size in res  
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        end = 0
        res = []
        size = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res