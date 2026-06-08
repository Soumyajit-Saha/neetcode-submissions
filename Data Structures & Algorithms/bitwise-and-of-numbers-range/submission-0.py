class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # stores num of 0 from right in res
        i = 0
        while left != right:
            # If starting from left side, left and right ar not equal then increase num of 0's from right
            left = left >> 1
            right = right >> 1
            i += 1

        return left << i