class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(opened, closed, comb):
            if closed == n:
                res.append(comb)
                return
            if opened == n:
                generate(opened, closed + 1, comb + ')')
            else:
                if opened > 0 and opened > closed:
                    generate(opened, closed + 1, comb + ')')
                generate(opened + 1, closed, comb + '(')

        generate(0, 0, '')
        return res
