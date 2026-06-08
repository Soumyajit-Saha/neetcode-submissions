class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        q = collections.deque()
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
                while q and l > q[0]:
                    q.popleft()

        return res
