class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        arr = [[0]*n for i in range(m)]

        if obstacleGrid[0][0] ==1 :
            return 0

        arr[0][0] =1

        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] ==1:
                    arr[i][j] = 0

                elif i==0  and  j== 0:
                    continue


               
                else:
                    arr[i][j] = (arr[i-1][j] if i > 0 else 0) + (arr[i][j-1] if j > 0 else 0)


        return arr[m-1][n-1]
        