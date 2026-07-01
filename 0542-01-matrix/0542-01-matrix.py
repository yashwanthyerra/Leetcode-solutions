from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []

        rows,cols = len(mat),len(mat[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append((i,j))
        
        visited = set(q)
      

        distance = 1    
        while q:

            size = len(q)
           
            curr = distance

            for i in range(size):
                r,c = q.popleft()
            

                # left
                if c-1 >= 0 and (r,c-1) not in visited and mat[r][c-1] != 0:
                    visited.add((r,c-1))
                    mat[r][c-1] = curr
                    q.append((r,c-1))

                # right
                if c+1 < cols  and (r,c+1) not in visited and mat[r][c+1] != 0:
                    visited.add((r,c+1))
                
                    mat[r][c+1] = curr  
                    q.append((r,c+1))   

                # up
                if r-1 >= 0  and (r-1,c) not in visited and mat[r-1][c] != 0:
                    visited.add((r-1,c))
           
                    mat[r-1][c] = curr
                    q.append((r-1,c))

                # down
                if r+1 < rows  and (r+1,c) not in visited and mat[r+1][c] != 0:
                    visited.add((r+1,c))
                  
                    mat[r+1][c] = curr
                    q.append((r+1,c))

            distance +=1

        return mat
        
        