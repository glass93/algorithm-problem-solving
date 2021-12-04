import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    data = list(map(int, input().split()))
    count = 0
    for i in range(n - 1):
        for j in range(i+1, n):
            if data[i] != data[j]:
                count += 1

    print(count)
