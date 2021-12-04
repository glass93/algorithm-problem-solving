# 틀린 풀이

import sys
sys.stdin = open('input.txt')

data = list(map(int, input()))

count = 0
for i in range(len(data)):
    if data[i] == 0:
        count += 1


result = 0
if count > int(len(data) / 2):
    for i in range(len(data)):
        if data[i] == 1:
            data[i] = 0
            result += 1
else:
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 1
            result += 1

print(result)