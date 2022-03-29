class Solution:
    def reverseString(self, s):
        """
        type s : List[str]
        type return : List[str]
        """
        left, right = 0, len(s) - 1


        def swap(left, right):
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp


        while left < right:
            swap(left, right)
            left += 1
            right -= 1
        