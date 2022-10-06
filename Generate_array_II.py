n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i%2==0):
        for j in range(l[i+1]):
            print(l[i],end=" ")