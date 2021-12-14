import sys
sys.stdin = open('input.txt')

A = list(map(int, input().split()))

A.sort()

for i in range(len(A)):
    if A[i] != i+1:
        print(0)

print(1)