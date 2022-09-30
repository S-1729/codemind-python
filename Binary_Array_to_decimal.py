n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    n-=1
    sum+=(2**n)*l[i]
print(sum)