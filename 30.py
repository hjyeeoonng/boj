a=input()
num=[]
for i in a:
    num.append(int(i))
num.sort()
if num[0]!=0:
    print(-1)
else:
    num.reverse()
    num.pop()
    count=0
    R=''
    for i in num:
        count+=i
    if count%3==0:
        for j in num:
            R+=str(j)
        R+='0'
    else:
        R='-1'
    print(int(R))
