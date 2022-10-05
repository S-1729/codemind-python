n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split()))[:m])
for i in range(n):
    max=0
    for j in range(m):
        if(l[j][i]>max):
            max=l[j][i]
    print(max)