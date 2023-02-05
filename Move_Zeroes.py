n=int(input())
l=list(map(int,input().split()))
z=[]
for i in l:
    if i!=0:
        print(i,end=" ")
for i in l:
    if i==0:
        print(i,end=" ")
    