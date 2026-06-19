class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0,0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row >= 0 and row < len(grid)
                        and col >= 0 and col < len(grid[0])
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append([row, col])
                
            time += 1

        return time if fresh == 0 else -1