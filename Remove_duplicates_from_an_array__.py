n=int(input())
l=list(map(int,input().split()))[:n]
l=list(set(l))
for i in l:
    print(i,end=" ")