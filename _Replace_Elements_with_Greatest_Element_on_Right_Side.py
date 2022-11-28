n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    max=-1
    for j in range(i+1,n):
        if arr[j]>max:
            max=arr[j]
    l.append(max)
print(*l)