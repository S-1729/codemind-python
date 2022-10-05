s=input()
maxi=0
for i in s:
    if i!=' ':
        if ord(i)>maxi:
            maxi=ord(i)
print(chr(maxi))