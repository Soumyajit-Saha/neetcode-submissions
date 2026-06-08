class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for asteroid in asteroids[1:]:
            while stack and (stack[-1] > 0 and asteroid < 0) and abs(asteroid) > stack[-1]:
                stack.pop()
            if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0) or (stack[-1] < 0 and asteroid > 0):
                stack.append(asteroid)
            elif stack and stack[-1] == abs(asteroid):
                stack.pop()
            else:
                continue


        return stack
