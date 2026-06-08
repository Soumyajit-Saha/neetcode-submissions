class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indStack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                ind = indStack.pop()
                res[ind] = i - ind
            stack.append(temperatures[i])
            indStack.append(i)

        return res