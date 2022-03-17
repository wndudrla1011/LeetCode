# solution 1
​class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()

        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]
        
# solution 2
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
