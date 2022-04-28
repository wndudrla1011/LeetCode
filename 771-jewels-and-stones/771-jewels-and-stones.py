class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        answer = 0

        # default value = 0
        freqs = collections.defaultdict(int)

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            answer += freqs[char]
                
        return answer