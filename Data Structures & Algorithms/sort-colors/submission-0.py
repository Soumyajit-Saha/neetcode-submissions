class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one = 0
        two = 0
        zero = 0

        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
            if num == 2:
                two += 1

        i = 0
        for c in range(zero):
            nums[i] = 0
            i += 1

        for c in range(one):
            nums[i] = 1
            i += 1

        for c in range(two):
            nums[i] = 2
            i += 1