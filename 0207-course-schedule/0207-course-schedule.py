from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if  len(prerequisites)==0:
            return True
        
        n = len(prerequisites)
        indegree = [0]*numCourses
        graph = defaultdict(list)
        q = deque()
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        


        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for neibor in graph[node]:
                indegree[neibor]-=1


                if indegree[neibor]==0:
                    q.append(neibor)
        if 0 not in topo:
            topo.append(0)

        return  len(topo)==numCourses