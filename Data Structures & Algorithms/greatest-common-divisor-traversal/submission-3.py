class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}
        self.components = n
    
    def find(self, n1):
        par = n1
        while par != self.parent[par]:
            par = self.parent[par]
        return par

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        self.components -= 1
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        unionFind = UnionFind(len(nums))

        factorToIndexMap = {}

        for i in range(len(nums)):
            j = 2
            while j * j <= nums[i]:
                if nums[i] % j == 0:
                    if j in factorToIndexMap:
                        unionFind.union(i, factorToIndexMap[j])
                    else:
                        factorToIndexMap[j] = i
                    while nums[i] % j == 0:
                        nums[i] = nums[i] // j

                j += 1

            if nums[i] != 1:
                if nums[i] in factorToIndexMap:
                    unionFind.union(i, factorToIndexMap[nums[i]])
                else:
                    factorToIndexMap[nums[i]] = i

        return unionFind.components == 1


        
        