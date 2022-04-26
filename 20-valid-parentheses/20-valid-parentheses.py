class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for elem in s:
            if elem == "(" or elem == "[" or elem == "{":
                stack.append(elem)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == "(" and elem == ")":
                        stack.pop()
                    elif stack[-1] == "{" and elem == "}":
                        stack.pop()
                    elif stack[-1] == "[" and elem == "]":
                        stack.pop()
                    else:
                        return False

        if not stack:
            return True
        else:
            return False