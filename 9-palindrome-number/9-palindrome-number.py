class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        left, right = 0, len(x) - 1

        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1

        return True