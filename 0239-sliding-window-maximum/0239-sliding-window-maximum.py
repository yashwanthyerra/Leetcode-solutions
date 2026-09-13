class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        curr = collections.deque()

        for i in range(len(nums)):

            while curr and curr[-1] < nums[i]:
                curr.pop()

            curr.append(nums[i])


            if i>=k and curr[0] == nums[i-k]:
                curr.popleft()

            if i >= k-1:
                result.append(curr[0])

        return result
        