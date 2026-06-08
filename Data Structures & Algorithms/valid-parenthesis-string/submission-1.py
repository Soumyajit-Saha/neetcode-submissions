class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = 0
        openMax = 0

        for c in s:
            if c == '(':
                openMin = openMin + 1
                openMax = openMax + 1

            elif c == ')':
                openMin = openMin - 1
                openMax = openMax - 1

            else:
                openMin = openMin - 1
                openMax = openMax + 1

            if openMax < 0:
                return False
            if openMin < 0:
                openMin = 0

        return openMin == 0