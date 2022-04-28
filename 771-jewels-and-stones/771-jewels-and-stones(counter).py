import collections

jewels = "aA"
stones = "aAAbbbb"
answer = 0

counter = collections.Counter(stones)

for j in jewels:
    if j in counter:
        answer += counter[j]

print(answer)
