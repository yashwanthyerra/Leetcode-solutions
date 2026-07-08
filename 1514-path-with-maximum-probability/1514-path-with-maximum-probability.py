from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph =defaultdict(list)
        
        best = [0]*n

        for i in range(len(edges)):
            edges[i].append(succProb[i])

        for u,v,w in edges:
            graph[u].append((-w,v))
            graph[v].append((-w,u))

        pq = [(1,start_node)]

        
        while pq:
            curr_prb ,node = heapq.heappop(pq)

            if node == end_node:
                return -curr_prb

            for w,v in graph[node]:
                prb = curr_prb*(w)
# just heap should append -ve values only so if and else are written
                if abs(prb)>abs(best[v]):     
                    best[v] = prb
                    if prb<0:
                        heapq.heappush(pq,(prb,v))
                    else:
                        heapq.heappush(pq,(-prb,v))
        return 0


                 




        

        


        





        