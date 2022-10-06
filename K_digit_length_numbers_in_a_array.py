n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    length=len(str(abs(i)))
    if(length==k):
        c+=1
print(c)