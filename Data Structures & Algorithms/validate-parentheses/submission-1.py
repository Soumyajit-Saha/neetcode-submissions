class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')': '(', '}': '{', ']': '['}

        for p in s:
            if p in [')', '}', ']']:
                if stack and stack[-1] == p_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if not stack else False