import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))

counter = [0] * N
max_counter = 0
max_turn = False

for i in range(len(A)):
    if A[i] == N+1:
        if max_turn == True:
            counter = [max_counter] * N
            max_turn = False
        else:
            continue
    else:
        counter[A[i]-1] += 1
        if counter[A[i]-1] > max_counter:
            max_counter = counter[A[i]-1]
            max_turn = True

print(counter)