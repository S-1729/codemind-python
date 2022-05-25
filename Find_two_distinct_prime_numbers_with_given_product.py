n=int(input())
fcount=0
for i in range(1,n):
    if n%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i,end=" ")
            fcount+=1
        if fcount==2:
            break
else:
    print(-1)