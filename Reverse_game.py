n=int(input())
l=list(map(int,input().split()))
for i in l:
    temp=i
    rev=0
    while(i>0):
        rem=i%10
        rev=rev*10+rem
        i//=10
    print(rev,end=" ")