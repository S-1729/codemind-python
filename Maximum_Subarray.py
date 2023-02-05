n=int(input())
l=list(map(int,input().split()))
maxi=l[0]
sum=0
for j in l:
    sum+=j
    if(sum>maxi):
        maxi=sum
    if(sum<0):
        sum=0
print(maxi)
