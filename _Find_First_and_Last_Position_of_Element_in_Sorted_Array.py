n=int(input())
arr=list(map(int,input().split()))
target=int(input())
first,last=-1,-1
for i in range(n):
    if arr[i]==target:
        first=i 
        break
for i in range(n-1,-1,-1):
    if arr[i]==target:
        last=i 
        break
print(first,last)