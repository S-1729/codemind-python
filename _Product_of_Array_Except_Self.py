n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    pro=1
    for j in range(n):
        if i!=j:
            pro*=arr[j]
    l.append(pro)
print(*l)