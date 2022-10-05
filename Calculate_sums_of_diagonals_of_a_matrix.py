n=int(input())
l=[]
sum1,sum2=0,0
for i in range(n):
    l.append(list(map(int,input().split()))[:n])
for i in range(n):
    for j in range(n):
        if(i==j):
            sum1+=l[i][j]
        if(i+j==n-1):
            sum2+=l[i][j]
print("Principal Diagonal:{}".format(sum1))
print("Secondary Diagonal:{}".format(sum2))