import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in range(len(nums)):

            heapq.heappush(heap,int(nums[i]))

            if len(heap)>k:
                heapq.heappop(heap)
            
        return str(heapq.heappop(heap))

            

            
            

                


        