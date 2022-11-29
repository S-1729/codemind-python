t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sortedd=sorted(arr)
    j1,j2=1,0
    for i in range(n):
        if i%2==0:
            arr[i]=sortedd[n-j1]
            j1+=1
        else:
            arr[i]=sortedd[j2]
            j2+=1
    print(*arr)