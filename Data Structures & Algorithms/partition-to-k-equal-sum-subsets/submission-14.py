class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        visit = set()
        n = len(nums)

        nums.sort()

        def dfs(start, subset, subsetSum):
            if subset == k:
                return True
            if subsetSum == target:
                return dfs(0, subset + 1, 0)
            for i in range(start, n):
                if i in visit or nums[i] + subsetSum > target:
                    continue
                visit.add(i)
                if dfs(i + 1, subset, subsetSum + nums[i]):
                    visit.remove(i)
                    return True
                visit.remove(i)
                if start == 0:
                    break
            return False

        return dfs(0, 0, 0)
