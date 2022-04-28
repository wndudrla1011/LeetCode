class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        table, answer = {}, 0

        for char in stones:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1

        for j in jewels:
            if j in table:
                answer += table[j]
                
        return answer