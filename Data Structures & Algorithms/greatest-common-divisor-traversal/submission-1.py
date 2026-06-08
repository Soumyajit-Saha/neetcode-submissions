# Intuition is to cosider each pair in nums as an edge and their indices as nodes.
# If any two pairs in nums has a common divisor > 1, we put the node in same connected component
# Now how to check if 2 nums have a common divisor
#   For each num in nums,
#       Check for factors from 2 to sqrt(num), if it divides nums
#           If it divides nums, map the factor to the index of the num
#               If there is already a number that this factor divides, connect this num with that number
#               This verifies we are connecting 2 nums having same factor
#               Keep on diving num with factor until not possible, to eliminate check for non-prime factors
#       The num left is also considerd as a factor, so do step 6 - 8 fot this
class UnionFind:
    def __init__(self, n):
        self.connectedComponents = n
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def getParent(self, node):
        par = node
        while par != self.parent[par]:
            par = self.parent[par]
        return par

    def union(self, u, v):
        p1, p2 = self.getParent(u), self.getParent(v)
        if p1 == p2:
            return False
        else:
            self.connectedComponents -= 1
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.parent[p1] = p2
                self.rank[p2] += self.rank[p1]
            return True


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_to_num_index = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_to_num_index:
                        uf.union(i, factor_to_num_index[f])
                    else:
                        factor_to_num_index[f] = i
                    while n % f == 0:
                        n //= f

                f += 1

            if n > 1:
                if n in factor_to_num_index:
                    uf.union(i, factor_to_num_index[n])
                else:
                    factor_to_num_index[n] = i
        return uf.connectedComponents == 1
        