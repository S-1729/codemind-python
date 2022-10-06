s=input()
l=s.split()
min=len(l[0])
for i in l:
    if(len(i)<min):
        min=len(i)
print(min)