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
        p1, p2 = self.getParent(n1), self.getParent(n2)
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
        for i, edge in enumerate(edges):
            edge.append(i)

        # Kruskal algo
        edges = sorted(edges, key=lambda e: e[2])

        mstWeight = 0
        uf = UnionFind(n)

        # Go over sorted edges
        for n1, n2, w, i in edges:
            # If the edge doesn't form a cycle, add it to mst
            if uf.union(n1, n2):
                mstWeight += w

        critical, pseudo = [], []
        for n1, n2, w, i in edges:
            # Exclude this edge
            weight = 0
            uf = UnionFind(n)

            # Go over sorted edges
            for v1, v2, eW, j in edges:
                # If the edge doesn't form a cycle and it is not the edge we are skipping, add it to mst
                if i != j and uf.union(v1, v2):
                    weight += eW

            # If we cannot form an mst without the edge or the mst weight gets bigger, it is critical
            if max(uf.rank.values()) != n or weight > mstWeight:
                critical.append(i)
                continue

            # Include this edge
            weight = w
            uf = UnionFind(n)
            uf.union(n1, n2)

            # Go over sorted edges
            for v1, v2, eW, j in edges:
                # If the edge doesn't form a cycle, add it to mst
                if uf.union(v1, v2):
                    weight += eW

            if weight == mstWeight:
                pseudo.append(i)

        return [critical, pseudo]

            



