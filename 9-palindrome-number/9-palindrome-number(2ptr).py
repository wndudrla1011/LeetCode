import sys

x = 5312135

x = str(x)

left, right = 0, len(x) - 1

while left < right:
    if x[left] != x[right]:
        print(False)
        sys.exit(0)
    left += 1
    right -= 1

print(True)
