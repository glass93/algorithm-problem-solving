import sys
sys.stdin = open('input.txt')

A = list(map(int, input().split()))

if len(A) == 1:
    print(A[0])

A.sort()
count = 1
answer = 0
for i in range(0, len(A)-1):
    if A[i] == A[i+1]:
        count += 1
    elif A[i] != A[i+1]:
        if count % 2:
            answer = A[i]
            break
        else:
            count = 1

    if i == len(A) -2 and count % 2:
        answer = A[i+1]

print(answer)