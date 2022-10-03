n=int(input())
s=str(n)
l=len(s)
if '6' in s:
    l=list(s)
    ind=l.index('6')
    l[ind]='9'
    s="".join(l)
    print(int(s))
else:
    print(n)