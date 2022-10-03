n=int(input())
l=list(map(int,input().split()))
c=0
for j in range(len(l)):
    if(l[j]%2==1):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")