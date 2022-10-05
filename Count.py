n=int(input())
l=list(map(int,input().split()))[:n]
c1,c2=0,0
for i in l:
    if(i%2==0):
        c1+=1
    else:
        c2+=1
print(c1,c2)