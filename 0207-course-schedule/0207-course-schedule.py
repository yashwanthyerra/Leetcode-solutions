from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numscourses = numCourses
        if  len(prerequisites)==0:
            return True


        n = len(prerequisites)

        indegree = [0]*numscourses

        graph = defaultdict(list)

        q = deque()

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1

        for i in range(numscourses):
            if indegree[i] == 0:
                q.append(i)


        topo = []

        while q :

            node = q.popleft()
            topo.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)


            
        return len(topo) == numscourses

