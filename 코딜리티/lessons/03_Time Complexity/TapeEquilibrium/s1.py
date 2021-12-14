import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))

minimum_value = 999999999

first = 0
second = sum(data)
for i in range(0, len(data)-1):
    first += data[i]
    second -= data[i]
    value = abs(first - second)
    if value < minimum_value:
        minimum_value = value



print(minimum_value)