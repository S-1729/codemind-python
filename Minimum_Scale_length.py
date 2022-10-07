def minimum(l,i):
    c=0
    for j in l:
        if(j%i==0):
            c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
for i in range(max(l),0,-1):
    if(minimum(l,i)==n):
        print(i)
        break
else:
    print("1")