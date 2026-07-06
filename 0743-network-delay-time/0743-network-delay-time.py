from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))

    
        time_taken= [float("inf")] * n

        time_taken[k-1] = 0

        pq = [(0,k)]

        while pq:
            curr_time,node = heapq.heappop(pq)

            if curr_time > time_taken[node-1]:
                continue
            
            for w,nei in graph[node]:
                new_time = curr_time + w

                if new_time < time_taken[nei-1]:
                    time_taken[nei-1] = new_time

                    heapq.heappush(pq,(new_time,nei))

        if float("inf") not in time_taken:
            result = max(time_taken)

            return result
        return -1



        