class Solution(object):
    def isPalindrome(self, s):
        """
        type s : str
        type return: bool
        """
        result = ""

        for char in s:
            if char.isalnum():
                result += char.lower()

        return result == result[::-1]
