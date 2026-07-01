from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows,cols = len(grid),len(grid[0])

        q = deque()

        count =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    count+=1

        time = 0
        while q:
            prev = count
            size = len(q)
            for i in range(size): 

                r,c = q.popleft()
                
                # left
                if c -1 >=0 and grid[r][c-1]==1:
                    grid[r][c-1] = 2
                    q.append((r,c-1))
                    count-=1

                # right 
                if c +1 < cols and  grid[r][c+1]==1:
                    grid[r][c+1] = 2
                    q.append((r,c+1))
                    count-=1

                # down
                if r+1 < rows and grid[r+1][c]==1:
                    grid[r+1][c] = 2
                    q.append((r+1,c))
                    count-=1

                # up
                if r-1 >=0 and  grid[r-1][c] ==1 :
                    grid[r-1][c] = 2
                    q.append((r-1,c))
                    count-=1
            
            if prev>count:
                time +=1

        if count==0:
            return time
        return -1
        
                
               


                    

        
