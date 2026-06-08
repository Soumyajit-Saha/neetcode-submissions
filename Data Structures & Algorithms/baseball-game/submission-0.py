class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                val = stack[-1]
                stack.append(2 * val)
            elif op == '+':
                op1 = stack[-1]
                op2 = stack[-2]
                stack.append(op1 + op2)
            else:
                stack.append(int(op))

        return sum(stack)

