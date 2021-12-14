import sys
sys.stdin = open('input.txt')

def push(X):
    stack.append(X)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        temp = stack.pop(-1)
        print(temp)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

# 명령의 수 N을 입력 받는다
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    else:
        top()
