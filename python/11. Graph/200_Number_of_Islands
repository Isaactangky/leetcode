# if there is a "1", bfs for all "1" of the same island
# and num += 1
# time: O(n), we are visiting every box for one time
# space: O(n), visited could store n coordiantes
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid) , len(grid[0])
        visited = set()
        num = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                direction = [[0, 1], [0, -1], [1, 0 ], [-1, 0]]
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (r in range(rows) 
                        and c in range(cols) and 
                        grid[r][c] == "1"
                        and (r, c) not in visited):
                        #mark the place as visited to avoid cycle
                            visited.add((r, c))
                            q.append((r, c))
                        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r , c) not in visited:
                    bfs(r, c)
                    num += 1
        return num
