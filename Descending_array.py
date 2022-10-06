n=int(input())
l=list(map(int,input().split()))
li=sorted(l)
for i in range(n):
    if(l[i]!=li[n-i-1]):
        print("no")
        break
else:
    print("yes")