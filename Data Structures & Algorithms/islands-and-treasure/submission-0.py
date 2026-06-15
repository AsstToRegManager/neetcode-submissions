class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def addToQueue(r, c):
            if (r in range(rows) and
                    c in range(cols) and
                    (r, c) not in visit and
                    grid[r][c] != -1):
                    visit.add((r, c))
                    q.append((r, c))

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addToQueue(r + 1, c)
                addToQueue(r - 1, c)
                addToQueue(r, c + 1)
                addToQueue(r, c - 1)
                    
            dist += 1


            

            

            


            
