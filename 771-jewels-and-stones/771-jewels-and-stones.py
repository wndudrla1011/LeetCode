class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        answer = 0

        table = collections.defaultdict(int)

        for S in stones:
            table[S] += 1

        for J in jewels:
            if table[J]:
                answer += table[J]
                
        return answer