class Solution:
    def numSquares(self, n: int) -> int:

        num = n
        while num % 4 == 0:
            num = num // 4

        if num % 8 == 7:
            return 4

        s = int(math.sqrt(n))
        if s * s == n:
            return 1

        i = 1
        while i * i <= n:
            firstSquare = i * i
            secondSquare = n - firstSquare
            s = int(math.sqrt(secondSquare))
            if s * s == secondSquare:
                return 2
            i += 1

        return 3