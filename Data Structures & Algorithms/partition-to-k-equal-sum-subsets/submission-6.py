class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k

        visited = set()

        def dfs(start, nthsubset, subsetSum):
            if nthsubset == k:
                return True
            if subsetSum == target:
                return dfs(0, nthsubset + 1, 0)
            for i in range(start, len(nums)):
                if i in visited or subsetSum + nums[i] > target:
                    continue
                visited.add(i)
                if dfs(i + 1, nthsubset, subsetSum + nums[i]):
                    return True
                visited.remove(i)

                if subsetSum == 0:
                    break

            return False
            

        return dfs(0, 0, 0)