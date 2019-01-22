k=int(input())
lt=list(map(int,input().split()))
lt.sort()
print(lt)
f=0
n=len(lt)
if len(lt)%2!=0:
    for i in range(n-1):
        if lt[i]+lt[n-1-i]!=lt[n-1]:
            f=f+1

else:
    for i in range(1,n-1):
    if lt[i]+lt[n-1-i]!=lt[0]+lt[n-1]:
        f=f+1



if f==0:
    print('Yes')
else:
    print('No')    


