import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()

    alpha = []
    num = []

    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            alpha.append(s[i])
        else:
            num.append(int(s[i]))

    alpha.sort()

    if len(num) != 0:
        result = "".join(alpha) + str(sum(num))
    else:
        result = "".join(alpha)

    print(result)