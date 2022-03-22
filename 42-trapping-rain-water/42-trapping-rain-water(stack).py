# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [2, 0, 0, 1, 2]
stack = []
volume = 0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not len(stack):
            break

        # distance -> horizontal
        distance = i - stack[-1] - 1
        # waters -> vertical
        waters = min(height[i], height[stack[-1]]) - height[top]
        # volume -> horizontal * vertical * height(2-dimensional -> except)
        volume += distance * waters

    stack.append(i)

print(volume)
