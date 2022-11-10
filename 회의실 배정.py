import sys
N=int(sys.stdin.readline())
Tlist=[]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    temp.append(temp[1]-temp[0])
    Tlist.append(temp)
print(Tlist)
Tlist.sort(key=lambda x:x[2])
print(Tlist)
