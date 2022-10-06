n=int(input())
l=list(map(int,input().split()))
a=int(input())
sum=0
for i in l:
    if(i!=a):
        sum+=i
    else:
        sum+=i
        break
print(sum)