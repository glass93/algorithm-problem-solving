import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))

counting = [0] * (len(data) + 2)

for i in range(len(data)):
    counting[data[i]] += 1

for i in range(1, len(counting)):
    if counting[i] == 0:
        print(i)

