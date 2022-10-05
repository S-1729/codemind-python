li=[]
n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(n):
    if(i<n//2):
        li.append(l[n-i-1])
    else:
        li.append(l[i-n//2])
print(*li)