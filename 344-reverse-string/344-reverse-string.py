class Solution:
    def reverseString(self, s):
        """
        type s : List[str]
        type return : List[str]
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        