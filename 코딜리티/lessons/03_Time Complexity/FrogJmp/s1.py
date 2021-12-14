import sys
sys.stdin = open('input.txt')

X, Y, D = map(int, input().split())

if X > Y:
    print(0)

temp_1 = int((Y-X) // D)
temp_2 = int((Y-X) % D)
if temp_2 == 0:
    print(temp_1)
else:
    print(temp_1+1)
