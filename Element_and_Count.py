n=int(input())
l=list(map(int,input().split()))
for i in sorted(set(l),key=l.index):
    print(i,end=" ")
    print(l.count(i),end=" ")
