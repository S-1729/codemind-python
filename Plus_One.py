n=int(input())
l=list(map(int,input().split()))[:n]
s=''
for i in l:
    s+=str(i)
m=int(s)+1
li=list(str(m))
print(*li)