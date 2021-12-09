import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    n = list(map(int, input()))

    length = int(len(n) / 2)

    front = n[:length:]
    end = n[length::]

    if sum(front) == sum(end):
        print("LUCKY")
    else:
        print("READY")