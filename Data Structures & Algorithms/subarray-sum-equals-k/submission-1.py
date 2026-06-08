class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        sumMap[0] = 1

        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            if currSum - k in sumMap:
                res += sumMap[currSum - k]
            
            sumMap[currSum] += 1
        
        return res
