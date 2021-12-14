import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = sys.stdin.readline().split()

    result = ""

    for i in range(len(s)):
        if s[i] == 1:
            result += s[i]
        else:
            result += s[i][::-1]
        result += " "

    print(result)