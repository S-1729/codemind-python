s=input()
s=s.lower()
c=0
for i in s:
    for j in s:
        if(i==j):
            c+=1
if(c==len(s)):
    print("True")
else:
    print("False")