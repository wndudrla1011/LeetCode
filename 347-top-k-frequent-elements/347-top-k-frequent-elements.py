class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ctr = collections.Counter(nums)
        avobe = []

        ctr = ctr.most_common()
        for i in range(len(ctr)):
            if k:
                avobe.append(ctr[i][0])
            else:
                break
            k -= 1
                
        return avobe