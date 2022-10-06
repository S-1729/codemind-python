n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    while(i>0):
        rem=i%10
        sum+=rem
        i//=10
print(sum)