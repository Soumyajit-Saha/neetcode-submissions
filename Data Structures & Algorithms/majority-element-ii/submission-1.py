class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            # There can be max 2 elements whose count can be greater than n/3.
            # As if there are 3 elements, there total count > n 
            if len(count) > 2:
                new_count = defaultdict(int)
                for n, c in count.items():
                    if c > 1:
                        new_count[n] = c - 1
                count = new_count

        res = []
        for n in count.keys():
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res