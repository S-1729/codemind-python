s=input()
c=0
for i in s:
    if(i.isalpha() or i.isnumeric()):
        continue
    else:
        if(i != ' '):
            c+=1
print(c)