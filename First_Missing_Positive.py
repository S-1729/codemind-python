n=int(input())
arr=list(map(int,input().split()))
arr.sort()
i=1
for x in arr:
    if x>0:
        if x!=i:
            break 
        i+=1
print(i)
    