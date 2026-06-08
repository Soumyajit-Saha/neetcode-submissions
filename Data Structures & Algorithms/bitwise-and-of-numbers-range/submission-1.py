class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # stores num of 0 from right in res
        i = 0
        # go on checking prefixes of left and right
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        # the prefix that is equal and right to that add i 0s
        return left << i