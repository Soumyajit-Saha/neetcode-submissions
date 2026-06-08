class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parentMap = {i: i for i in range(1, len(edges) + 1)}
        rank = {i: 1 for i in range(1, len(edges) + 1)}

        def findParent(node):
            parent = node
            while parent != parentMap[parent]:
                parent = parentMap[parent]
            return parent

        def join(u, v):
            p1 = findParent(u)
            p2 = findParent(v)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parentMap[p2] = p1
                rank[p1] += rank[p2]

            else:
                parentMap[p1] = p2
                rank[p2] += rank[p1]

            return True

        for u, v in edges:
            if join(u, v) == False:
                return [u, v]
