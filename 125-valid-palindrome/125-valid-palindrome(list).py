class Solution(object):
    def isPalindrome(self, s):
        subject = []

        for char in s:
            if char.isalnum():
                subject.append(char.lower())

        while len(subject) > 1:
            if subject.pop(0) != subject.pop():
                return False

        return True