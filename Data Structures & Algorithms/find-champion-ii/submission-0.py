class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = {i: 0 for i in range(n)}

        for u, v in edges:
            indegree[v] += 1

        count = 0
        res = -1
        for i in range(n):
            if indegree[i] == 0:
                count += 1
                res = i

        if count > 1:
            return -1
        return res