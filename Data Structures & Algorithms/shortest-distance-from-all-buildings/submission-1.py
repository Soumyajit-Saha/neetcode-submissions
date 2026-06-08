class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # 1. BFS from Empty Land to All Houses
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        totalHouses = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalHouses += 1

        def bfs(row, col):
            q = deque()
            q.append((row, col, 0))

            housesVisited = 0
            distance = 0

            visited = set()

            while q and housesVisited != totalHouses:
                size = len(q)

                for _ in range(size):
                    r, c, dist = q.popleft()

                    if (r, c) in visited:
                        continue

                    visited.add((r, c))
                    
                    if grid[r][c] == 1:
                        housesVisited += 1
                        distance += dist
                        continue

                    for ri, ci in dirs:
                        if 0 <= r + ri < len(grid) and 0 <= c + ci < len(grid[0]) and grid[r + ri][c + ci] in [0, 1]:
                            q.append((r + ri, c + ci, dist + 1))

            if housesVisited != totalHouses:
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 0 and (i, j) in visited:
                            grid[i][j] = 2
                return float('inf')

            return distance


        minDist = float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    minDist = min(minDist, bfs(i, j))

        return minDist if minDist != float('inf') else -1