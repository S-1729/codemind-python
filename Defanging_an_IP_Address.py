string=input()
s=""
for i in string:
    if(i=='.'):
        s+="[.]"
    else:
        s+=i
print(s)