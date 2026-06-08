class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def eval(op1, op2, sign):
            if sign == '+':
                return op1 + op2
            elif sign == '*':
                return op1 * op2
            elif sign == '-':
                return op1 - op2
            else:
                return int(float(op1) / op2)
                

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                second = stack.pop()
                first = stack.pop()

                res = eval(first, second, token)
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[-1]