class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def calculate(num):
            s = 0
            while num > 0:
                d = num % 10
                s += d**2
                num = num // 10
            return s

        while n != 1:
            val = calculate(n)
            if val in visited:
                return False
            visited.add(val)
            n = val

        return True