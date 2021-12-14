import sys
sys.stdin = open('input.txt')

A = list(map(int, input().split()))

sorted_A = sorted(A)

if len(sorted_A) == 1:
    if sorted_A[0] < 1 or sorted_A[0] > 1:
        print(1)
    else:
        print(2)

if not 1 in sorted_A:
    print(1)

if sorted_A[-1] < 1:
    print(1)

try:
    start = sorted_A.index(1)
    for i in range(start, len(sorted_A)-1):
        difference = sorted_A[i] - sorted_A[i+1]

        if difference == 0 or difference == -1:
            continue
        else:
            print(sorted_A[i]+1)
    print(sorted_A[-1]+1)
except:
    print(1)