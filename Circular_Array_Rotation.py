n,k,q=list(map(int,input().split()))
l=list(map(int,input().split()))[:n]
arr=l[-k:]+l[:-k]
for i in range(q):
    m=int(input())
    print(arr[m])