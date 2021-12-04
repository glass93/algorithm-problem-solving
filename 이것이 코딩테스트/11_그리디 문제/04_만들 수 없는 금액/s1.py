import sys
sys.stdin = open('input.txt')
from itertools import combinations

n = int(input())

data = list(map(int, input().split()))
ordered_data = sorted(data)

count_list = [0] * 1000001

print(ordered_data)
for i in range(1, len(data)):
    combi = list(combinations(data, i))
    for j in range(len(combi)):
        if count_list[sum(combi[j])] == 0:
            count_list[sum(combi[j])] = 1

print(count_list[1:15].index(0) + 1)