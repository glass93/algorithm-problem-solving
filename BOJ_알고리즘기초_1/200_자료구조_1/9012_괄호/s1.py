import sys
sys.stdin = open('input.txt')

T = int(input())

def check_VPS(data):
    stack = []
    for i in range(len(data)):
        if data[i] == "(":
            stack.append(data[i])
        elif data[i] == ")" and len(stack) == 0:
            return "NO"
        elif data[i] == ")" and stack[-1] == "(":
            stack.pop()

    if len(stack):
        return "NO"
    else:
        return "YES"


for tc in range(1, T+1):
    data = sys.stdin.readline()

    print(check_VPS(data))