class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        # reverse sort pairs in reverse order of position i.e near ones come first
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            timeToReach = (target - p) / s
            # if the car further from previous car in position takes less or same time, it can catch the previous car, so we remove the previous car as both of them are in a fleet, as previous car is slower, we don't add the current car time in the stack
            if stack and stack[-1] >= timeToReach:
                continue
            else:
                stack.append(timeToReach)

        return len(stack)