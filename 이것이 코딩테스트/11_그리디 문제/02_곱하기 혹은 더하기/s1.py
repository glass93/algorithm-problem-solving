import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    data = list(map(int, input()))

    result = data[0]

    for i in range(1, len(data)):
        if result == 0:
            result += data[i]
        else:
            if data[i] == 0 or data[i] == 1:
                result += data[i]
            else:
                result *= data[i]

    print(result)