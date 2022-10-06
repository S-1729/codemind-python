n=int(input())
a=list(map(int,input().split()))
a=set(a)
sum=0
for i in a:
    if(i%2==1):
        sum+=i
print(sum)