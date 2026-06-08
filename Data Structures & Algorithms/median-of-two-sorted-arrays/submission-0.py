class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(nums1) - 1

        while True:
            mid1 = l + (r - l) // 2
            # we assume the left partitions in both arrays should have half of total no of items
            # the partion is assume to be [0 - mid][mid + 1: end]
            # since index starts from 0, 
            #   total number of items in left part of nums1 = mid1 + 1
            #   total number of items in left part of nums2 = mid2 + 1
            #   half = mid1 + 1 + mid2 + 1 
            #   mid2 = half - mid1 -2
            mid2 = half - mid1 - 2

            left1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            right1 = nums1[mid1 + 1] if mid1 < len(nums1) - 1 else float('inf')

            left2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            right2 = nums2[mid2 + 1] if mid2 < len(nums2) - 1 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1




