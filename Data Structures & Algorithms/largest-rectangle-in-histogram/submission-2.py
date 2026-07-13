class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        indStack = []
        res = float('-inf')

        for i, height in enumerate(heights):
            ind = i
            while stack and stack[-1] > height:
                ind = indStack.pop()
                item = stack.pop()
                res = max(res, item * (i - ind))

            stack.append(height)
            indStack.append(ind)

        for i in range(len(stack) - 1, -1, -1):
            res = max(res, stack[i] * (len(heights) - indStack[i]))

        return res
