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

        slow = n
        fast = calculate(n)

        while fast != slow:
            fast = calculate(calculate(fast))
            slow = calculate(slow)

        return True if fast == 1 else False