s=input()
c=0
for i in s:
    if(i.isalnum()==False):
        if(i is not ' '):
            c+=1
print(c)