class Solution(object):
    def isPalindrome(self, s):
        """
        type s : str
        type return: bool
        """
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
