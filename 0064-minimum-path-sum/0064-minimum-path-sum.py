class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        arr = [[float("inf")]*n for _ in range(m)]

        arr[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):

                if i==0 and j==0:
                    continue

                #left 
                if j-1 >= 0 :
                    arr[i][j] = min(arr[i][j-1]+grid[i][j],arr[i][j])
                #right
                if j+1 < n : 
                    arr[i][j] = min(arr[i][j+1]+ grid[i][j],arr[i][j])
                #down
                if i+1 < m: 
                    arr[i][j] = min(arr[i+1][j]+grid[i][j],arr[i][j])
                #up
                if i-1 >= 0: 
                    arr[i][j] = min(arr[i-1][j]+grid[i][j],arr[i][j])

        return arr[m-1][n-1]

        