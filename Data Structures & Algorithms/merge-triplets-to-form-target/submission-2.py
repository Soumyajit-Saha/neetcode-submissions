class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # The intuition is to check if any position if any triplet equals to that position in the target
        # And not involving any triplet whose any position value is greater than the target position.
        gotFirst = False
        gotSecond = False
        gotThird = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                gotFirst = True
            if t[1] == target[1]:
                gotSecond = True
            if t[2] == target[2]:
                gotThird = True

        return gotFirst and gotSecond and gotThird
