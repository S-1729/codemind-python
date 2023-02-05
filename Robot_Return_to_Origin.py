s=input()
c1,c2,c3,c4=0,0,0,0
for i in s:
    if(i=='L'):
        c1+=1
    elif(i=='R'):
        c2+=1
    elif(i=='U'):
        c3+=1
    else:
        c4+=1
if(c1==c2 and c3==c4):
    print("True")
else:
    print("False")