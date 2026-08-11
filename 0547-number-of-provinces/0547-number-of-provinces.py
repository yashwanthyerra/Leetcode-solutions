
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(node):
            visited[node] = True

            for nei in range(n):
                if isConnected[node][nei] ==1 and not visited[nei]:
                    dfs(nei)

        provinces = 0
        for city in range(n):
            if not visited[city]:
                provinces+=1
                dfs(city)

        return provinces
        
        
  