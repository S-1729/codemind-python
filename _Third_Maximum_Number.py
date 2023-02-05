n=int(input())
l=list(map(int,input().split()))
arr=sorted(list(set(l)))
if(len(arr)>=3):
    print(arr[-3])
else:
    print(arr[1])