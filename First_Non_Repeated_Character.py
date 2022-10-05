t=int(input())
for i in range(t):
    n=int(input())
    s=input()[:n]
    s=s.lower()
    for j in s:
        if(s.count(j)==1):
            print(j,end="
")
            break
    else:
        print("-1")