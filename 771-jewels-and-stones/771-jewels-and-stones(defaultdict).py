import collections

jewels = "aA"
stones = "aAAbbbb"
answer = 0

# default value = 0
freqs = collections.defaultdict(int)

for char in stones:
    freqs[char] += 1

for char in jewels:
    answer += freqs[char]

print(answer)