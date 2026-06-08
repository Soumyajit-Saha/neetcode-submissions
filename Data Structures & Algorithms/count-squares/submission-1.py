class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = set()

    def add(self, point: List[int]) -> None:
        self.pointsCount[(point[0], point[1])] += 1
        self.points.add((point[0], point[1]))

        
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        res = 0
        for p in self.points:
            px = p[0]
            py = p[1]
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.pointsCount[(px, py)] * self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        return res
