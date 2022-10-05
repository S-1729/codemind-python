n=int(input())
m=int(input())
l=[]
sum=0
for i in range(n):
    l.append(list(map(int,input().split()))[:m])
for i in range(n):
    for j in range(m):
        sum+=l[i][j]
print(sum)