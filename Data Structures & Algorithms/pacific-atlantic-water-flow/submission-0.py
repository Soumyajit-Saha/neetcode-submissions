class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        def dfsPacific(i, j, prev):
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]) or (i, j) in pacific or heights[i][j] < prev:
                return
            pacific.add((i, j))

            prev = heights[i][j]
            dfsPacific(i + 1, j, prev)
            dfsPacific(i - 1, j, prev)
            dfsPacific(i, j + 1, prev)
            dfsPacific(i, j - 1, prev)

        atlantic = set()
        def dfsAtlantic(i, j, prev):
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]) or (i, j) in atlantic or heights[i][j] < prev:
                return
            atlantic.add((i, j))

            prev = heights[i][j]
            dfsAtlantic(i + 1, j, prev)
            dfsAtlantic(i - 1, j, prev)
            dfsAtlantic(i, j + 1, prev)
            dfsAtlantic(i, j - 1, prev)

        for i in range(len(heights)):
            dfsPacific(i, 0, float('-inf'))
            dfsAtlantic(i, len(heights[0]) - 1, float('-inf'))

        for j in range(len(heights[0])):
            dfsPacific(0, j, float('-inf'))
            dfsAtlantic(len(heights) - 1, j, float('-inf'))

        intersect = pacific.intersection(atlantic)

        return [[i, j] for i, j in intersect]
        