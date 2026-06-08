class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, r1, l2, r2):
            i1 = l1
            i2 = l2

            temp = []
            while i1 <= r1 and i2 <= r2:
                if nums[i1] < nums[i2]:
                    temp.append(nums[i1])
                    i1 += 1
                else:
                    temp.append(nums[i2])
                    i2 += 1

            while i1 <= r1:
                temp.append(nums[i1])
                i1 += 1

            while i2 <= r2:
                temp.append(nums[i2])
                i2 += 1

            j = 0
            for i in range(l1, r2 + 1):
                nums[i] = temp[j]
                j += 1

        def mergeSort(l, r):
            if l < r:
                mid = l + (r - l) // 2
                mergeSort(l, mid)
                mergeSort(mid + 1, r)
                merge(l, mid, mid + 1, r)

        mergeSort(0, len(nums) - 1)
        return nums
            