class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def getParent(self, node):
        par = node
        while par != self.parent[par]:
            par = self.parent[par]
        return par

    def union(self, n1, n2):
        p1 = self.getParent(n1)
        p2 = self.getParent(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        uf = UnionFind(n)

        for i, edge in enumerate(edges):
            edge.append(i)

        mst = 0
        edges.sort(key=lambda x: x[2])

        for u, v, w, i in edges:
            if uf.union(u, v):
                mst += w

        critical, pseudo = [], []

        for u1, v1, w1, i1 in edges:
            uf = UnionFind(n)
            mstCritical = 0
            for u2, v2, w2, i2 in edges:
                if i2 == i1:
                    continue
                if uf.union(u2, v2):
                    mstCritical += w2
            
            if max(uf.rank.values()) < n or mstCritical > mst:
                critical.append(i1)
                continue

            uf = UnionFind(n)
            mstPseudo = w1
            uf.union(u1, v1)

            for u2, v2, w2, i2 in edges:
                if i2 == i1:
                    continue
                if uf.union(u2, v2):
                    mstPseudo += w2

            if mstPseudo == mst:
                pseudo.append(i1)

        return [critical, pseudo]

