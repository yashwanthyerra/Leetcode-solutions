import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col = len(heights) ,len(heights[0])
        
        graph = [[float("inf")]*col for i in range(row)]

        graph[0][0] = 0

        min_heap = [(0,0,0)]

        while min_heap:
                
            abs_dif,r,c = heapq.heappop(min_heap)

            curr = abs_dif

            if r== row-1 and c== col-1:
                return abs_dif

            if abs_dif > graph[r][c]:
                continue

            # left
            if c >0:
                new_effort = max(curr , abs(heights[r][c] - heights[r][c-1]))
                if new_effort < graph[r][c-1]:
                    graph[r][c-1] = new_effort
                    heapq.heappush(min_heap,(new_effort,r,c-1))
                    

            # right
            if c<col-1:
                new_effort = max(curr , abs(heights[r][c] - heights[r][c+1]))
                if new_effort< graph[r][c+1]:
                    graph[r][c+1] = new_effort
                    heapq.heappush(min_heap,(new_effort,r,c+1))
                
            # up
            if r>0:
                new_effort= max(curr , abs(heights[r][c] - heights[r-1][c]))
                if new_effort < graph[r-1][c]:
                    graph[r-1][c] = new_effort
                    heapq.heappush(min_heap,(new_effort,r-1,c))

            # down
            if r<row-1:
                new_effort = max(curr , abs(heights[r][c] - heights[r+1][c]))
                if new_effort < graph[r+1][c]:
                    graph[r+1][c] = new_effort
                    heapq.heappush(min_heap,(new_effort,r+1,c))

        return 0
                







        
        