class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = [n]

        parentMap = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}

        def findParent(node):
            parent = parentMap[node]

            while parent != parentMap[parent]:
                parent = parentMap[parent]

            return parent

        def join(u, v):
            parent1 = findParent(u)
            parent2 = findParent(v)

            if parent1 == parent2:
                return

            if rank[parent1] > rank[parent2]:
                parentMap[parent2] = parent1
                rank[parent1] += rank[parent2]

            else:
                parentMap[parent1] = parent2
                rank[parent2] += rank[parent1]

            res[0] -= 1

        for edge in edges:
            join(edge[0], edge[1])

        return res[0]



            
