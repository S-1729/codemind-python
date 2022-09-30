n=int(input())
l=list(map(int,input().split()))
sum,c=0,0
for i in range(n):
    sum+=l[i]
avg=sum//n
for i in range(n):
    if(l[i]>=avg):
        c+=1
print(c)