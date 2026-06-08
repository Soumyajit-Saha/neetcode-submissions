class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        indexStack = []

        res = 0

        for i in range(len(heights)):
            ind = i
            while stack and stack[-1] > heights[i]:
                greaterHeight = stack.pop()
                ind = indexStack.pop()
                res = max(res, greaterHeight * (i - ind))

            stack.append(heights[i])
            indexStack.append(ind)

        for i in range(len(stack) - 1, -1, -1):
            res = max(res, stack[i] * (len(heights) - indexStack[i]))

        return res