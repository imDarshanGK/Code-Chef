n = int(input())
for i in range(n):
    X, Y = map(int, input().split())
    if X>=Y:
        print("YES")
    else:
        print("NO")
