class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ctr = collections.Counter(nums)
        avobe = []

        for key, value in ctr.most_common():
            if k:
                avobe.append(key)
            else:
                break
            k -= 1
        
        return avobe