class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = collections.Counter(stones)

        result = 0
        for J in jewels:
            if counter[J]:
                result += counter[J]
                
        return result