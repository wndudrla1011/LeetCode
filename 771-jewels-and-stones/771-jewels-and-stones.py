class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        answer = 0

        counter = collections.Counter(stones)

        for j in jewels:
            if j in counter:
                answer += counter[j]
                
        return answer