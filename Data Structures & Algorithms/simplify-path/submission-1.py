class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        paths = path.split('/')

        for curr in paths:
            if curr == '' or curr == '.':
                continue
            if curr == '..':
                if stack: 
                    stack.pop()
            else:
                stack.append(curr)

        return '/' + '/'.join(stack)

                