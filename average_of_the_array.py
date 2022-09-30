n=int(input())
l=list(map(int,input().split()))[:n]
sum=0
for i in range(n):
    sum+=l[i]
avg=sum/n
print("%.2f"%avg)
