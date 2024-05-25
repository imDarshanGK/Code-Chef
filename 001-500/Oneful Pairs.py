a,b = map(int,input().split())

# write your code here
pair_sum = a + b + (a * b)
if pair_sum == 111:
    print("Yes")
else: 
    print("No")
