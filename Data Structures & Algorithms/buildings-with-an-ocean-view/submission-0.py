class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        heights = [(height, i) for i, height in enumerate(heights)]

        stack = []

        for h, i in heights:
            while stack and stack[-1][0] <= h:
                stack.pop()
            stack.append((h, i))

        return [s[1] for s in stack]