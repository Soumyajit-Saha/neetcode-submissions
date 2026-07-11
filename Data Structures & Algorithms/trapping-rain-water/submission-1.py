class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                if height[l] < leftMax:
                    res += leftMax - height[l]
                else:
                    leftMax = height[l]
            else:
                r -= 1
                if height[r] < rightMax:
                    res += rightMax - height[r]
                else:
                    rightMax = height[r]

        return res