import sys
sys.stdin = open('input.txt')

X = int(input())
A = list(map(int, input().split()))

counting = [0] * (X+1)
result = 0
for i in range(X+1):
    result += i
for i in range(len(A)):
    if counting[A[i]] == 0:
        counting[A[i]] += 1
        result -= A[i]

    if result == 0:
        print(i)

if result != 0:
    print(-1)