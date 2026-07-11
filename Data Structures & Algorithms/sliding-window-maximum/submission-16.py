class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)

            if r - l + 1 == k:
                res.append(nums[q[0]])
                if l == q[0]:
                    q.popleft()
                l += 1
        
        return res