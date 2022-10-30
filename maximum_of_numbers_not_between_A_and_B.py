n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
max=-1;
for i in l:
    if(i<a or i>b):
        if(i>max):
            max=i
print(max)