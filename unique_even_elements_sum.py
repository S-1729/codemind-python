n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
sum=0
for i in a:
    if(i%2==0):
        sum+=i
print(sum)