import sys

s = "({})"

stack = []

for elem in s:
    if elem == "(" or elem == "[" or elem == "{":
        stack.append(elem)
    else:
        if not stack:
            print(False)
            sys.exit(0)
        else:
            if stack[-1] == "(" and elem == ")":
                stack.pop()
            elif stack[-1] == "{" and elem == "}":
                stack.pop()
            elif stack[-1] == "[" and elem == "]":
                stack.pop()
            else:
                print(False)
                sys.exit(0)

if not stack:
    print(True)
else:
    print(False)