class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ongoingProduct = 1
        res = [ongoingProduct]
        for i in range(1, len(nums)):
            ongoingProduct *= nums[i - 1]
            res.append(ongoingProduct)

        ongoingProductRight = 1
        for i in range(len(nums) - 2, -1, -1):
            ongoingProductRight *= nums[i + 1]
            res[i] = res[i] * ongoingProductRight

        return res