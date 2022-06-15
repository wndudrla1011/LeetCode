class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Q = []
        result = []

        for n in nums:
            heapq.heappush(Q, -n)

        for _ in range(len(Q)):
            result.append(-heapq.heappop(Q))

        return result[k-1]