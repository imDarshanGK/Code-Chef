# The code below is incorrect. Debug the code to solve this problem

T=int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if X == Y and (X>0 or Y>0):
        print('YES')
    else:
        print('NO')
    
