class Solution:

    def dfs(self,curr_node, visited, graph , color):

        visited[curr_node] = color

        for nei in graph[curr_node]:
            if visited[nei] != -1 :

                if visited[nei] == color:
                    return False

            else: 
                ans  = self.dfs(nei,visited,graph,1-color)
                if ans == False:
                    return False

        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:

        n = len(graph)
        visited = [-1] * n 

        for index in range(0,n):
            if visited[index] == -1 :
                ans = self.dfs(index, visited , graph , 0 )
                if ans == False :
                    return False

        return True 
        
