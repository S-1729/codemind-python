s=input()
s=s.lower()
c=0
v="aeiou"
for i in range(len(s)-1,-1,-1):
    if s[i] in v:
        c+=1
print(c)