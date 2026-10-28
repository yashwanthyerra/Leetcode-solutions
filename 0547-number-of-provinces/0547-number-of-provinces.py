class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        provinces = 0 

        for city in range(n ):
            if not visited[city]:
                provinces += 1

            stk = [city]
            while stk:
                node = stk.pop()
                if visited[node]:
                    continue

                visited[node] = True

            
                for nei in range(n):
                    if isConnected[node][nei] == 1 and not visited[nei]:
                        stk.append(nei)


        return provinces