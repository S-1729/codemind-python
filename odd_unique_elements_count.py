n=int(input())
l=list(map(int,input().split()))
l=list(set(l))
c=0
for i in l:
    if(i%2==1):
        c+=1
print(c)