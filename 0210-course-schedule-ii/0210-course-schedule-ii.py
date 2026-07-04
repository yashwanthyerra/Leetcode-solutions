from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses

        graph = defaultdict(list)

        q = deque()

        for u,v in  prerequisites:
            graph[v].append(u)
        
            indegree[u] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        topo= []
         
        while q:
            node = q.popleft()

            topo.append(node)

            for nei in graph[node]:
                indegree[nei] -=1

                if indegree[nei]==0:
                    q.append(nei)
        if len(topo)==numCourses:
            return topo
        return []


        