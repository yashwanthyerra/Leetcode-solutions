import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col = len(heights) ,len(heights[0])

        min_heap =  [(0,0,0)]

        visit = set()

        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        while min_heap:

            diff,r,c = heapq.heappop(min_heap)

            if (r,c) in visit:
                continue

            visit.add((r,c))

            if (r,c) == (row-1,col-1):
                return diff

            for dr , dc in directions:

                nr , nc = r+dr , c+dc   # new r , new c

                if (nr<0 or nc< 0 or nr==row or nc == col or (nr,nc) in visit):
                    continue

                new_diff = max(diff, abs( heights[r][c]-heights[nr][nc] ))
                heapq.heappush(min_heap,(new_diff,nr,nc))

            






        
        