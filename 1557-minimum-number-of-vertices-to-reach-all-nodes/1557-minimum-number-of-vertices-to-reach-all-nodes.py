from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0]*n

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            in_degree[v]+=1

        ans =[]

        for i in range(n):
            if in_degree[i]==0:
                ans.append(i)
        return ans

        